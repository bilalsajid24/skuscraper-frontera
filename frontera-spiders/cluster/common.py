from __future__ import absolute_import
from frontera.settings.default_settings import MIDDLEWARES

MAX_NEXT_REQUESTS = 512
SPIDER_FEED_PARTITIONS = 2  # Spider Instances
SPIDER_LOG_PARTITIONS = 2   # SW Instances

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

QUEUE_HOSTNAME_PARTITIONING = True
KAFKA_LOCATION = 'localhost:9092'

URL_FINGERPRINT_FUNCTION = 'frontera.utils.fingerprint.hostname_local_fingerprint'
MESSAGE_BUS = 'frontera.contrib.messagebus.kafkabus.MessageBus'

SPIDER_LOG_TOPIC = 'frontier-done'
SPIDER_FEED_TOPIC = 'frontier-todo'
SCORING_TOPIC = 'frontier-score'
