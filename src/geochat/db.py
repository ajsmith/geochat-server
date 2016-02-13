import logging

import geoalchemy2
import sqlalchemy
import sqlalchemy.orm

import geochat.config
import geochat.message
import geochat.user

_log = logging.getLogger(__name__)


def create():
    engine = sqlalchemy.create_engine(db_url('postgres'))
    conn = engine.connect()
    conn.execute('COMMIT;')
    conn.execute('CREATE DATABASE geochat;')
    conn.execute('CREATE ROLE geochat WITH LOGIN;')
    conn.execute('GRANT ALL ON DATABASE geochat TO geochat;')
    conn.close()
    _log.info('Created database.')


def init():
    engine = get_engine()
    conn = engine.connect()
    conn.execute('CREATE EXTENSION postgis;')
    conn.close()
    _log.info('Created postgis extensions.')

    for cls in (geochat.user.User, geochat.message.Message):
        cls.__table__.create(engine)
        _log.info('Created %s table.', cls.__name__)


def db_url(db_name):
    config = geochat.config.get()
    host = config.db_host
    port = config.db_port
    user = config.db_user
    return 'postgresql+psycopg2://%s@%s:%s/%s' %  (user, host, port, db_name)


def get_engine():
    return sqlalchemy.create_engine(db_url('geochat'))


def session_factory():
    return sqlalchemy.orm.sessionmaker(bind=get_engine())


def get_session():
    return session_factory()()
