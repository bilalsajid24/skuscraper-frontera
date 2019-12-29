from scrapy.spiders import Spider, Request
from ..items import HackerNewsItem


class HackernewsSpider(Spider):
    name = 'hackernews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        for item_s in response.css('.itemlist .athing'):
            item = HackerNewsItem()
            item['url'] = item_s.css('.storylink::attr(href)').get()
            item['title'] = item_s.css('.storylink::text').get()
            item['item_id'] = item_s.css('::attr(id)').get()
            yield item

        next_url = response.css('[rel="next"]::attr(href)')

        if not next_url:
            yield None

        next_url = response.urljoin(next_url.get())
        yield Request(next_url, callback=self.parse)