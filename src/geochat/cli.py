"""\
Command Line Interface (CLI) capabilities.
"""

import argparse
import sys

import geochat.config
import geochat.db
import geochat.web


def createdb():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--host',
        dest='db_host',
        default='127.0.0.1',
        help='Database server host.',
    )
    parser.add_argument(
        '--port',
        dest='db_port',
        type=int,
        default=5432,
        help='Database server port.',
    )
    parser.add_argument(
        '--user',
        dest='db_user',
        default='geochat',
        help='Database user.',
    )

    args = parser.parse_args()
    geochat.config.update(
        db_host=args.db_host,
        db_port=args.db_port,
        db_user=args.db_user,
    )
    geochat.db.create()


def initdb():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--host',
        dest='db_host',
        default='127.0.0.1',
        help='Database server host.',
    )
    parser.add_argument(
        '--port',
        dest='db_port',
        type=int,
        default=5432,
        help='Database server port.',
    )
    parser.add_argument(
        '--user',
        dest='db_user',
        default='geochat',
        help='Database user.',
    )

    args = parser.parse_args()
    geochat.config.update(
        db_host=args.db_host,
        db_port=args.db_port,
        db_user=args.db_user,
    )
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
        default=5432,
        help='Database server port.',
    )
    parser.add_argument(
        '--db-user',
        dest='db_user',
        default='geochat',
        help='Database user.',
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
        db_host=args.db_host,
        db_port=args.db_port,
        db_user=args.db_user,
        http_port=args.http_port,
    )

    geochat.web.serve()
