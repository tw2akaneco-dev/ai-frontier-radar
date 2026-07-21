"""Content analysis using AI."""

import asyncio
import html
import json
import re
from typing import List, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn

from .client import AIClient
from .prompts import CONTENT_ANALYSIS_SYSTEM, CONTENT_ANALYSIS_USER
from .utils import parse_json_response
from ..models import ContentItem

DEFAULT_THROTTLE_SEC = 0.0


class ContentAnalyzer:
    """Analyzes content items using AI to determine importance."""

    def __init__(self, ai_client: Optional[AIClient] = None):
        self.client = ai_client

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    def _get_throttle_sec(self) -> float:
        """Return the configured inter-item throttle, clamped to zero or above."""
        config = getattr(self.client, "config", None)
        throttle_sec = getattr(config, "throttle_sec", DEFAULT_THROTTLE_SEC)
        return max(throttle_sec, 0.0)

    @staticmethod
    def _plain_text(value: str) -> str:
        value = value.split("--- Top Comments ---", 1)[0]
        value = re.sub(r"<[^>]+>", " ", value)
        value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
        value = re.sub(r"\s+", " ", html.unescape(value)).strip()
        if len(value) <= 320:
            return value
        return value[:317].rsplit(" ", 1)[0] + "..."

    @staticmethod
    def _rule_tags(item: ContentItem) -> tuple[List[str], float]:
        text = item.title.lower()
        groups = [
            ("mcp", 0.8, ("mcp", "model context protocol")),
            ("agent", 0.6, ("agent", "agentic", "coding assistant", "computer use", "browser use")),
            ("model", 0.4, ("llm", "model", "gpt", "claude", "gemini", "qwen", "transformer")),
            ("inference", 0.5, ("inference", "reasoning", "vllm", "ollama", "llama.cpp", "serving")),
            ("research", 0.3, ("paper", "benchmark", "arxiv", "dataset", "training")),
            ("open-source", 0.3, ("open source", "open-source", "github", "release")),
        ]
        tags = []
        relevance = 0.0
        for tag, weight, terms in groups:
            if any(term in text for term in terms):
                tags.append(tag)
                relevance += weight
        category = item.metadata.get("category")
        if category and category not in tags:
            tags.append(str(category))
        return tags[:6], min(relevance, 1.5)

    def _analyze_item_with_rules(self, item: ContentItem) -> None:
        meta = item.metadata
        tags, relevance = self._rule_tags(item)
        source = item.source_type.value
        score = 5.0
        reasons = []

        if source == "github":
            score = 7.4
            reasons.append("受监控项目发布新版本")
            if meta.get("prerelease"):
                score -= 0.8
                reasons.append("预发布版本")
        elif source == "rss":
            score = 6.6
            category_weights = {
                "frontier-labs": 1.6,
                "mcp": 1.5,
                "open-source": 1.0,
                "ai-engineering": 0.8,
                "ai-industry": 0.7,
                "ai-news": 0.7,
                "research": -1.1,
            }
            score += category_weights.get(str(meta.get("category") or ""), 0.3)
            feed_name = str(meta.get("feed_name") or "")
            if feed_name == "Awesome MCP Servers":
                score -= 1.2
            elif feed_name == "MCP Protocol Commits":
                score += 0.3
            reasons.append(f"来自 {meta.get('feed_name') or 'RSS'}")
        elif source == "hackernews":
            popularity = float(meta.get("score") or 0)
            comments = float(meta.get("descendants") or 0)
            score = 5.3 + min(popularity / 100, 1.8) + min(comments / 75, 0.8)
            if relevance == 0:
                score = min(score, 6.8)
            reasons.append(f"Hacker News {int(popularity)} 分")
        elif source == "reddit":
            popularity = float(meta.get("score") or 0)
            comments = float(meta.get("num_comments") or 0)
            subreddit = str(meta.get("subreddit") or "")
            community_bonus = {"mcp": 1.1, "LocalLLaMA": 0.5, "MachineLearning": 0.3}.get(subreddit, 0.2)
            score = 5.0 + community_bonus + min(popularity / 100, 1.6) + min(comments / 75, 0.8)
            reasons.append(f"r/{subreddit} {int(popularity)} 分")

        score += relevance
        if tags:
            reasons.append("主题匹配 " + "、".join(tags[:3]))

        item.ai_score = round(max(0.0, min(score, 10.0)), 1)
        item.ai_reason = "；".join(reasons) or "规则评分"
        item.ai_tags = tags

        excerpt = self._plain_text(item.content or "")
        if excerpt:
            item.ai_summary = excerpt
        elif source == "github":
            item.ai_summary = f"项目 {meta.get('repo') or item.title} 发布版本 {meta.get('tag') or ''}。"
        else:
            item.ai_summary = item.title

    async def analyze_batch(self, items: List[ContentItem]) -> List[ContentItem]:
        if self.client is None:
            for item in items:
                self._analyze_item_with_rules(item)
            return items

        throttle_sec = self._get_throttle_sec()
        analyzed_items = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Analyzing", total=len(items))

            for index, item in enumerate(items):
                try:
                    await self._analyze_item(item)
                    analyzed_items.append(item)
                except Exception as e:
                    print(f"Error analyzing item {item.id}: {e}")
                    item.ai_score = 0.0
                    item.ai_reason = "Analysis failed"
                    item.ai_summary = item.title
                    analyzed_items.append(item)
                progress.advance(task)
                if throttle_sec > 0 and index < len(items) - 1:
                    await asyncio.sleep(throttle_sec)

        return analyzed_items

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=10)
    )
    async def _analyze_item(self, item: ContentItem) -> None:
        """Analyze a single content item.

        Args:
            item: Content item to analyze (modified in-place)
        """
        # Prepare content section
        content_section = ""
        if item.content:
            # Split off comments if present
            content_text = item.content
            if "--- Top Comments ---" in content_text:
                main, comments_part = content_text.split("--- Top Comments ---", 1)
                content_section = f"Content: {main.strip()[:800]}"
            else:
                content_section = f"Content: {content_text[:1000]}"

        # Prepare discussion section (comments, engagement)
        discussion_parts = []
        if item.content and "--- Top Comments ---" in item.content:
            comments_part = item.content.split("--- Top Comments ---", 1)[1]
            discussion_parts.append(f"Community Comments:\n{comments_part[:1500]}")

        meta = item.metadata
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"score: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} comments")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} likes")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} retweets")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} replies")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} views")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} bookmarks")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"upvote ratio: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"Engagement: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"Discussion: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"Community Note: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        # Generate user prompt
        user_prompt = CONTENT_ANALYSIS_USER.format(
            title=item.title,
            source=f"{item.source_type.value}",
            author=item.author or "Unknown",
            url=str(item.url),
            content_section=content_section,
            discussion_section=discussion_section
        )

        # Get AI completion
        response = await self.client.complete(
            system=CONTENT_ANALYSIS_SYSTEM,
            user=user_prompt,
        )

        # Parse JSON response with robust fallback
        result = self._parse_json_response(response)
        if result is None:
            print(f"Warning: could not parse analysis response for {item.id}, using defaults")
            item.ai_score = 0.0
            item.ai_reason = "Analysis response parse failed"
            item.ai_summary = item.title
            item.ai_tags = []
            return

        # Update item with analysis results
        item.ai_score = float(result.get("score", 0))
        item.ai_reason = result.get("reason", "")
        item.ai_summary = result.get("summary", item.title)
        item.ai_tags = result.get("tags", [])
