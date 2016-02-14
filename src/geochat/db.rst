==============
Database Tests
==============

The following tests cover basic database setup.

    >>> import geochat.config
    >>> import geochat.db
    [log] shapely.geos DEBUG Trying `CDLL(libgeos_c.so.1)`
    [log] shapely.geos DEBUG Library path: 'libgeos_c.so.1'
    [log] shapely.geos DEBUG DLL: <CDLL 'libgeos_c.so.1', handle ... at ...>
    [log] shapely.geos DEBUG Trying `CDLL(libc.so.6)`
    [log] shapely.geos DEBUG Library path: 'libc.so.6'
    [log] shapely.geos DEBUG DLL: <CDLL 'libc.so.6', handle ... at ...>

Create the database and database user.

    >>> geochat.config.update(db_user='postgres')
    >>> geochat.db.create()
    [log] geochat.db INFO Created database.
    [log] geochat.db INFO Created postgis extensions.

Iinitialize the database.

    >>> geochat.config.update(db_user='geochat')
    >>> geochat.db.init()
    [log] geochat.db INFO Created User table.
    [log] geochat.db INFO Created Message table.
