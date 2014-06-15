import crypt
import hashlib
import uuid

import sqlalchemy

import geochat.ormbase


def get_by_token(session, token):
    (user,) = session.query(User).filter(User.token == token)
    return user


def login(session, name, password):
    result = session.query(User).filter(User.name == name)
    if result:
        (user,) = result
        if user.check_password(password):
            user.login(password)
            return user
    return None


BaseUser = sqlalchemy.ext.declarative.declarative_base()


class User(geochat.ormbase.Base):
    """A user."""

    __tablename__ = 'users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.Sequence('users_id_seq'),
        primary_key=True,
    )
    registered = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))
    name = sqlalchemy.Column(sqlalchemy.Text)
    shadow = sqlalchemy.Column(sqlalchemy.Text)
    token = sqlalchemy.Column(sqlalchemy.Text)

    def set_password(self, password, old_password=None):
        if not bool(self.shadow) or self.check_password(old_password):
            self.shadow = crypt.crypt(password)
        else:
            raise Exception('Invalid password')

    def check_password(self, password):
        salt = '$'.join(self.shadow.split('$')[:-1])
        return self.shadow == crypt.crypt(password, salt=salt)

    def login(self, password):
        if self.check_password(password):
            self.token = hashlib.sha512(uuid.uuid4().hex).hexdigest()
        else:
            raise Exception('Invalid password')

    def logout(self):
        self.token = None
