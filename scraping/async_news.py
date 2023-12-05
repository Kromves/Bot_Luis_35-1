import httpx
from parsel import Selector
import asyncio
from typing import List
from database import sql_commands

class AsyncNewsScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    MAIN_URL = "https://www.prnewswire.com/news-releases/news-releases-list/?page={page}&pagesize=25"
    LINK_XPATH = '//div[@class="card col-view"]/a/@href'
    PLUS_URL = 'https://www.prnewswire.com'
    IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'

    TEMPLATE_CONTAINS_XPATH = '//a[contains(@id, "app-show-episode-title")]'

    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def parse_pages(self, limit: int = 3) -> List[str]:
        async with httpx.AsyncClient(headers=self.headers) as client:
            urls = []
            async for page in self.async_generator(limit):
                urls.extend(await self.get_url(client, self.MAIN_URL.format(page=page)))

            return urls

    async def get_url(self, client, url):
        response = await client.get(url=url)
        return await self.scrape_responses(response)

    async def scrape_responses(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()
        return [self.PLUS_URL + link for link in links]


if __name__ == "__main__":
    async def main():
        scraper = AsyncNewsScraper()
        data = await scraper.parse_pages(limit=3)

    asyncio.run(main())
