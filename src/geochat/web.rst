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

    >>> response = app.post('/register', {'username': 'Bilbo', 'password': 'secret'})
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


Login
=====

Log in the user.

    >>> print app.post('/login', {'username': 'Bilbo', 'password': 'secret'}, status='*')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8
    Set-Cookie: geochat.auth.token=...; Path=/
    Hello, Bilbo!


Say Message
===========

Say a message in the area.

    >>> data = {'author': 'Sauron', 'body': 'Where did I put that ring?', 'location': 'POINT(38.884218 -76.995027)'}
    >>> print app.post('/say', data, status='*')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8

Say a few more messages.

    >>> data = {
    ...     'author': u'Bilbo',
    ...     'body': u'I found the ring!',
    ...     'location': 'POINT(38.8951 -77.0367)',
    ... }
    >>> print app.post('/say', data, status='*')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8

    >>> data = {
    ...     'author': u'Bilbo',
    ...     'body': u'Just buying groceries!',
    ...     'location': 'POINT(38.889075 -77.091012)',
    ... }
    >>> print app.post('/say', data, status='*')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8

    >>> data = {
    ...     'author': u'Bilbo',
    ...     'body': u'Having a latte!',
    ...     'location': 'POINT(38.890214 -77.086039)',
    ... }
    >>> print app.post('/say', data, status='*')
    Response: 200 OK
    Content-Type: text/html; charset=UTF-8


Local Messages
==============

Get messages in the area.

    >>> print app.get('/local', {'location': 'POINT(38.884218 -76.995027)'}, status='*')
    Response: 200 OK
    Content-Type: application/json
    {"local_messages": [{"data": {"body": "Where did I put that ring?", "location_wkt": "POINT (38.8842179999999971 -76.9950269999999932)", "author": "Sauron", "id": 1, "created": "..."}, "data_type": "message"}]}

    >>> print app.get('/local', {'location': 'POINT(38.889546 -77.035244)'})
    Response: 200 OK
    Content-Type: application/json
    {"local_messages": [{"data": {"body": "I found the ring!", "location_wkt": "POINT (38.8950999999999993 -77.0366999999999962)", "author": "Bilbo", "id": 2, "created": "..."}, "data_type": "message"}]}
