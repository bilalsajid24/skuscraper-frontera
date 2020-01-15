from scrapy.spiders import Spider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import HackerNewsItem


class HackernewsSpider(Spider):
    name = 'hackernews'

    rules = (
        Rule(LinkExtractor(restrict_css=['.morelink']), callback='parse'),
    )

    def parse(self, response):
        for item_s in response.css('.itemlist .athing'):
            item = HackerNewsItem()
            item['url'] = item_s.css('.storylink::attr(href)').get()
            item['title'] = item_s.css('.storylink::text').get()
            item['item_id'] = item_s.css('::attr(id)').get()
            yield item
