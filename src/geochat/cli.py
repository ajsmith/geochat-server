"""\
Command Line Interface (CLI) capabilities.
"""

import argparse
import sys

import geochat.config
import geochat.db
import geochat.web


def initdb():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--db-host',
        dest='db_host',
        default='127.0.0.1',
        help='Database server host.',
    )
    parser.add_argument(
        '--db-port',
        dest='db_port',
        type=int,
        default=10000,
        help='Database server port.',
    )

    args = parser.parse_args()
    geochat.config.update(db_host=args.db_host, db_port=args.db_port)
    geochat.db.init()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--db-host',
        dest='db_host',
        default='127.0.0.1',
        help='Database server host.',
    )
    parser.add_argument(
        '--db-port',
        dest='db_port',
        type=int,
        default=10000,
        help='Database server port.',
    )
    parser.add_argument(
        '--http-port',
        dest='http_port',
        type=int,
        default=8080,
        help='Port to run the HTTP server on.',
    )

    args = parser.parse_args()
    geochat.config.update(
        db_host=args.db_host, db_port=args.db_port, http_port=args.http_port,
    )

    geochat.web.serve()
