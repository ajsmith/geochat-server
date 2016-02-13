==============
Database Tests
==============

The following tests cover basic database setup.

    >>> import geochat.config
    >>> import geochat.db

Create the database and database user.

    >>> geochat.config.update(db_host='db', db_user='postgres')
    >>> geochat.db.create()
    [log] geochat.db INFO Created database.

Iinitialize the database.

    >>> geochat.config.update(db_host='db', db_user='geochat')
    >>> geochat.db.init()
    [log] geochat.db INFO Created postgis extensions.
    [log] geochat.db INFO Created User table.
    [log] geochat.db INFO Created Message table.
