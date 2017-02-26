# -*- coding: utf-8 -*-
from datetime import datetime
from pony.orm import *
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
as Serializer, BadSignature, SignatureExpired)
import config

db = Database()

class User(db.Entity):
    username = Required(unicode)
    password = Required(unicode)
    email = Required(unicode)
    dt_registered = Optional(datetime, default=datetime.now)
    dt_last_visit = Optional(datetime, default=datetime.now)
    verified = Required(bool, default=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self):
        s = Serializer(config.SECRET_KEY, expires_in=31622400)
        return s.dumps({'id': self.id})


    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        if not data['id']:
            return None
        user = User[data['id']]
        return user
