import datetime
import json

import bottle
import waitress

import geochat.config
import geochat.db
import geochat.message
import geochat.user


def serve():
    web_api = geochat.web.WebAPI()
    config = geochat.config.get()
    waitress.serve(web_api.app, host='0.0.0.0', port=config.http_port)


class WebAPI(object):

    def __init__(self, config=None):
        self.session = geochat.db.get_session()
        self.app = bottle.Bottle()

        self.app.get('/', callback=self.root)
        self.app.get('/local', callback=self.local)

        self.app.post('/register', callback=self.register)
        self.app.post('/login', callback=self.login)
        self.app.post('/say', callback=self.say)
        self.app.post('/logout', callback=self.logout)

    def root(self):
        return 'root!'

    def register(self):
        request = bottle.request
        username = request.params['username']
        password = request.params['password']
        user = geochat.user.User(name=username)
        user.set_password(password)
        user.login(password)
        self.session.add(user)
        self.session.commit()

        response = bottle.response
        response.set_cookie('geochat.auth.token', user.token, path='/')

    def login(self):
        request = bottle.request
        username = request.params['username']
        password = request.params['password']
        user = geochat.user.login(self.session, username, password)
        if user:
            self.session.commit()
            response = bottle.response
            response.set_cookie('geochat.auth.token', user.token, path='/')
        return 'Hello, %s!' % username

    def say(self):
        request = bottle.request
        auth_cookie = request.get_cookie('geochat.auth.token')
        user = geochat.user.get_by_token(self.session, auth_cookie)
        message = geochat.message.Message(
            created=datetime.datetime.now(),
            user_id=user.id,
            **dict(request.params)
            )
        self.session.add(message)
        self.session.commit()

    def local(self):
        request = bottle.request
        location = request.params['location']
        local_messages = geochat.message.get_local(self.session, location)
        return {
            'local_messages': [m.to_json_object() for m in local_messages],
        }

    def logout(self):
        request = bottle.request
        auth_cookie = request.get_cookie('geochat.auth.token')
        user = geochat.user.get_by_token(self.session, auth_cookie)
        user.logout()
        self.session.commit()
        bottle.response.delete_cookie('geochat.auth.token')
        return 'Goodbye.'
