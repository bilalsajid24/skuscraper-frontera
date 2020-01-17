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

1) In `settings.py` set `FRONTERA_SETTINGS` to `cluster.spider`

2) Install Kafka and Hbase
- `brew install kafka`
- `brew install hbase`

3) Start zookeeper, kafka and hbase
- `/usr/local/bin/start-hbase.sh`
- `zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties` (Make sure to start zookeeper server first)
- `kafka-server-start /usr/local/etc/kafka/server.properties`
- `/usr/local/bin/hbase thrift start`

4) Create namespace in Hbase
- `hbase shell`
- `create_namespace 'crawler'`
- `list_namespace`

5) Create Kafka topice
- `kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic frontier-done`
Set the number of partitions equal to number of strategy worker instances
- `kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic frontier-todo`
Set the number of partitions equal to number of spider instances
- `kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic frontier-score`

6) Start DBW
-  `python -m frontera.worker.db --config cluster.dbw --no-incoming --partitions 0`

7) Start SW (Upto N)
- `python -m frontera.worker.strategy --config cluster.sw --partition-id 0`

8) Add seed urls to DB
- `python -m frontera.utils.add_seeds --config cluster.spider --seeds-file vans_seed_urls.txt`

9) Start a single spider per spider feed partition (Upto N)
- `scrapy crawl vans-fr-crawler -s SPIDER_PARTITION_ID=1`
