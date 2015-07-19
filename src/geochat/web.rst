=======
Web API
=======

Clients interface with services via this web API.

    >>> import webtest
    >>> import geochat.web

    >>> app = webtest.TestApp(geochat.web.WebAPI().app)
    >>> response = app.get('/')
    >>> print response
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    root!


Register
========

Register a new user.

    >>> response = app.post('/register', {'username': 'Bilbo', 'password': 'secret1'})
    >>> print response
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=...; Path=/
    >>> auth_cookie = response.headers['Set-Cookie']

The GET method is disallowed.

    >>> app.get('/register')
    Traceback (most recent call last):
    AppError: Bad response: 405 Method Not Allowed (not 200 OK or 3xx redirect for http://localhost/register)

    >>> print app.post('/logout')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=-1
    Goodbye.

    >>> response = app.post('/register', {'username': 'Sauron', 'password': 'secret2'})
    >>> print response
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=...; Path=/
    >>> auth_cookie = response.headers['Set-Cookie']

    >>> print app.post('/logout')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=-1
    Goodbye.


Login
=====

Log in the user.

    >>> print app.post('/login', {'username': 'Bilbo', 'password': 'secret1'})
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=...; Path=/
    Hello, Bilbo!

    >>> print app.post('/logout')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=-1
    Goodbye.


Say Message
===========

Say a message in the area.

    >>> print app.post('/login', {'username': 'Sauron', 'password': 'secret2'})
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=...; Path=/
    Hello, Sauron!

    >>> data = {'body': 'Where did I put that ring?', 'location': 'POINT(38.884218 -76.995027)'}
    >>> print app.post('/say', data, status='*')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8

Say a few more messages.

    >>> print app.post('/login', {'username': 'Bilbo', 'password': 'secret1'})
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=...; Path=/
    Hello, Bilbo!

    >>> data = {
    ...     'body': u'I found the ring!',
    ...     'location': 'POINT(38.8951 -77.0367)',
    ... }
    >>> print app.post('/say', data)
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8

    >>> data = {
    ...     'body': u'Just buying groceries!',
    ...     'location': 'POINT(38.889075 -77.091012)',
    ... }
    >>> print app.post('/say', data)
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8

    >>> data = {
    ...     'body': u'Having a latte!',
    ...     'location': 'POINT(38.890214 -77.086039)',
    ... }
    >>> print app.post('/say', data)
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8


Local Messages
==============

Get messages in the area.

    >>> print app.get('/local', {'location': 'POINT(38.884218 -76.995027)'}, status='*')
    Response: 200 OK
    Content-Type: application/json
    {"local_messages": [{"data": {"body": "Where did I put that ring?", "location_wkt": "POINT (38.884218 -76.99502699999999)", "author": "Sauron", "id": 1, "created": "..."}, "data_type": "message"}]}

    >>> print app.get('/local', {'location': 'POINT(38.889546 -77.035244)'})
    Response: 200 OK
    Content-Type: application/json
    {"local_messages": [{"data": {"body": "I found the ring!", "location_wkt": "POINT (38.8951 -77.0367)", "author": "Bilbo", "id": 2, "created": "..."}, "data_type": "message"}]}

