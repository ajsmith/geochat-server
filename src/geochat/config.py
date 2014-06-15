"""\
Configuration capabilities.
"""


def get():
    return _config


def update(**options):
    _config.__dict__.update(options)


class Config(object):

    def __init__(self, **options):
        self.__dict__.update(options)


# Configuration singleton.
_config = Config()
