from __future__ import absolute_import


BACKEND = 'frontera.contrib.backends.sqlalchemy.Distributed'
SQLALCHEMYBACKEND_ENGINE = 'sqlite:///seeds.sqlite'
SQLALCHEMYBACKEND_ENGINE_ECHO = False
SQLALCHEMYBACKEND_DROP_ALL_TABLES = False
SQLALCHEMYBACKEND_CLEAR_CONTENT = False

DELAY_ON_EMPTY = 20.0
