# skuscraper-frontera
Distributed crawling for long running crawlers

# Sinlge Process

1) Add urls to seed url file

2) Run `python -m frontera.utils.add_seeds --config skuscraper.frontera.settings --seeds-file vans_seed_urls.txt`

3) Start the crawl `scrapy crawl vans-fr-crawler`
