from setuptools import setup, find_packages

entry_points = """\
[console_scripts]
geochat-createdb=geochat.cli:createdb
geochat-initdb=geochat.cli:initdb
geochatd=geochat.cli:main
"""

setup(
    name='geochat',
    version='0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite='geochat.tests.suite',
    entry_points=entry_points,
    install_requires=[
        'GeoAlchemy2',
        'SQLAlchemy',
        'Shapely',
        'WebTest',
        'bottle',
        'psycopg2',
        'waitress',
    ],
)
