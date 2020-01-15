from scrapy import Field, Item


class VansItem(Item):
    uuid = Field()
    brand = Field()
    care = Field()
    category = Field()
    description = Field()
    gender = Field()
    image_urls = Field()
    name = Field()
    price = Field()
    currency = Field()
    retailer_sku = Field()
    skus = Field()
    url = Field()
    url_orignal = Field()
    market = Field()
    retailer = Field()
    date = Field()
    crawl_id = Field()
    industry = Field()
    product_hash = Field()
    spider_name = Field()
    crawl_start_time = Field()
    meta = Field()


class HackerNewsItem(Item):
    url = Field()
    title = Field()
    item_id = Field()
