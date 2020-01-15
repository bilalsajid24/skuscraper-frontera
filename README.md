# skuscraper-frontera
Distributed crawling for long running crawlers

# Sinlge Process

1) In `settings.py` set `FRONTERA_SETTINGS` to `config.single`

2) Add urls to seed url file i.e `vans_seed_urls.txt`

3) Run `python -m frontera.utils.add_seeds --config config.single --seeds-file vans_seed_urls.txt` to store urls in DB

4) Start the crawl `scrapy crawl vans-fr-crawler`


# Distributed

1) In `settings.py` set `FRONTERA_SETTINGS` to `config.spider`

2) Add urls to seed url file i.e `vans_seed_urls.txt`

3) Start ZeroMQ broker `python -m frontera.contrib.messagebus.zeromq.broker`

3) Run `python -m frontera.utils.add_seeds --config config.dbw --seeds-file vans_seed_urls.txt` to store urls in DB

4) Start stratrgey worker `python -m frontera.worker.strategy --config config.sw`

5) Start the crawl `scrapy crawl vans-fr-crawler`

6) Start database worker `python -m frontera.worker.db --no-incoming --config config.dbw --partitions 0`

# Cluster Processing
