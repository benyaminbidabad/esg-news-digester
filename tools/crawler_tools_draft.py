from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import os
from pathlib import Path
import asyncio
from crawl4ai import AsyncWebCrawler

async def download_multiple_files(url: str, download_path: str):
    config = BrowserConfig(accept_downloads=True, downloads_path=download_path)
    async with AsyncWebCrawler(config=config) as crawler:
        run_config = CrawlerRunConfig(
            js_code="""
                console.log("Executing JavaScript code...");
                const downloadLinks = document.querySelectorAll('a[href$=".pdf"]');
                console.log(`Found ${downloadLinks.length} PDF links.`);
                for (const link of downloadLinks) {
                    console.log(`Clicking link: ${link.href}`);
                    link.click();
                    // Delay between clicks
                    await new Promise(r => setTimeout(r, 2000));  
                }
            """,
            wait_for="10"  # Wait for all downloads to start
        )
        result = await crawler.arun(url=url, config=run_config)

        if result.downloaded_files:
            print("Downloaded files:")
            for file in result.downloaded_files:
                print(f"- {file}")
        else:
            print("No files downloaded.")

# Usage
download_path = os.path.join(Path.home(), ".crawl4ai", "downloads")
os.makedirs(download_path, exist_ok=True)

asyncio.run(download_multiple_files("https://www.societegenerale.com/sites/default/files/documents/2025-02/20250224-communique-societe-generale-nomination-groupe.pdf", download_path))