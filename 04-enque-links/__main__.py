import asyncio

from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext


async def main() -> None:
    # Let's limit our crawls to make our tests shorter and safer.
    crawler = BeautifulSoupCrawler(max_requests_per_crawl=10)

    @crawler.router.default_handler
    async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
        url = context.request.url
        title = context.soup.title.string if context.soup.title else ''
        context.log.info(f'The title of {url} is: {title}.')

        # The default behavior of enqueue_links is to stay on the same hostname, so it does not require
        # any parameters. This will ensure the subdomain stays the same.
        # Find all links on the page (elements with <a> tag) and enqueue them.
        # Especially you can filter them by a CSS selector such as selector='a.article-link'
        await context.enqueue_links(strategy='same-domain')

    await crawler.run(['https://crawlee.dev/'])


if __name__ == '__main__':
    asyncio.run(main())
