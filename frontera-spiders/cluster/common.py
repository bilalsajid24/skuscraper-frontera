from __future__ import absolute_import
from frontera.settings.default_settings import MIDDLEWARES

MAX_NEXT_REQUESTS = 512
SPIDER_FEED_PARTITIONS = 1 # number of spider processes
SPIDER_LOG_PARTITIONS = 1 # worker instances

DELAY_ON_EMPTY = 5.0

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

QUEUE_HOSTNAME_PARTITIONING = True
KAFKA_LOCATION = 'localhost:9092'
SCORING_TOPIC = 'frontier-score'
URL_FINGERPRINT_FUNCTION = 'frontera.utils.fingerprint.hostname_local_fingerprint'
