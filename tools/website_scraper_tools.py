from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import os
from pathlib import Path
import asyncio
from crawl4ai import AsyncWebCrawler
from langchain.tools import tool

class CrawlWebsiteTools:
    @tool("Scrape a Website")
    def scrape_website(url: str) -> str:
        """Crawl a given website and return its content."""
    
        async def crawl():
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url)
                return result.markdown

        # Create a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Run the asynchronous crawl function within the new event loop
        content = loop.run_until_complete(crawl())
        return content

