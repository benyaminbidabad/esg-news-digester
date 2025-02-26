from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import os
from pathlib import Path
import asyncio
from crawl4ai import AsyncWebCrawler

async def CrawlWebsite(url):
    config = BrowserConfig()
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return print(result.markdown)

asyncio.run(CrawlWebsite("https://benyaminbidabad.fr"))