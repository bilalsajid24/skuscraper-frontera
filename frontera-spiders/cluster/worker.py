from __future__ import absolute_import
from .common import *

BACKEND = 'frontera.contrib.backends.hbase.HBaseBackend'

# HBASE_DROP_ALL_TABLES = True
# HBASE_USE_SNAPPY = False

MAX_NEXT_REQUESTS = 2048
NEW_BATCH_DELAY = 3.0

HBASE_THRIFT_HOST = 'localhost'
HBASE_THRIFT_PORT = 9090
