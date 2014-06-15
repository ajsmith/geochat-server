==========
User Tests
==========

    >>> import geochat.user

    >>> user = geochat.user.User(name='Bilbo')
    >>> user.name
    'Bilbo'

    >>> user.shadow is None
    True
    >>> user.set_password('secret')
    >>> 'secret' in user.shadow
    False
    >>> len(user.shadow.split('$'))
    4
    >>> user.check_password('secret')
    True
    >>> user.check_password('nope')
    False

We can't set a new password simply by providing a new one.

    >>> user.set_password('newsecret')
    Traceback (most recent call last):
    TypeError: must be string, not None
    >>> user.check_password('newsecret')
    False

We need to also provide the old password to change it.

    >>> user.set_password('newsecret', 'secret')
    >>> user.check_password('newsecret')
    True
    >>> user.check_password('secret')
    False

Obviously, the old password must also be valid for it to work.

    >>> user.set_password('newnewsecret', 'wrong')
    Traceback (most recent call last):
    Exception: Invalid password
    >>> user.check_password('newnewsecret')
    False

The old password still works.

    >>> user.check_password('newsecret')
    True
