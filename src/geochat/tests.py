"""\
Test harness.
"""

import doctest
import logging
import sys

import geochat.config


class StdoutStream(object):
    """Stream that simply writes to stdout.

    This allows us to simulate logging to stdout in doctests, and doctest
    changes the stdout object during test runs.
    """

    def write(self, msg):
        sys.stdout.write(msg)

    def close(self):
        nope


def setUp(test):
    # Set up logging
    logger = logging.getLogger()
    assert not logger.handlers
    handler = logging.StreamHandler(StdoutStream())
    format = "[log] %(name)s %(levelname)s %(message)s"
    handler.setFormatter(logging.Formatter(fmt=format))
    logger.addHandler(handler)
    logger.setLevel(0)

    # Configure the application.
    geochat.config.update(db_host='db', db_port=5432, http_port=8080)


def tearDown(test):
    root_log = logging.getLogger()
    del root_log.handlers[:]


def suite():
    return doctest.DocFileSuite(
        'db.rst', 'web.rst', 'user.rst',
        setUp=setUp,
        tearDown=tearDown,
        optionflags=(
            doctest.ELLIPSIS
            | doctest.IGNORE_EXCEPTION_DETAIL
            | doctest.NORMALIZE_WHITESPACE
        ),
    )
