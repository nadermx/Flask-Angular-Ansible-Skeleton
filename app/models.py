# -*- coding: utf-8 -*-
from datetime import datetime
from pony.orm import *
from werkzeug.security import generate_password_hash, check_password_hash

db = Database()

class User(db.Entity):
    username = Required(unicode)
    password = Required(unicode)
    email = Required(unicode)
    dt_registered = Required(datetime, default=datetime.now)
    dt_last_visit = Required(datetime, default=datetime.now)

    def setPassword(self, password):
        self.password = generate_password_hash(password)


    def checkPassword(self, password):
        if not self.password:
            return False
        return check_password_hash(self.password, password)
