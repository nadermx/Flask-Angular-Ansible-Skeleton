# -*- coding: utf-8 -*-
import os

# Statement for enabling the development environment
DEBUG = True
DOMAIN = 'domain.com'
DOMAIN_TITLE = 'Domain'
MAILGUN = 'randomapikey123'
# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
# Database configuration. These parameters are passed directly to db.bind().
DB_PROVIDER = 'sqlite'
DB_CONFIG = {
  'filename': 'db.sqlite',
  'create_db': True,
}
# DB_PROVIDER = 'postgres'
# DB_CONFIG = {
#   'user': 'user',
#   'password': 'password',
#   'database' :'database',
#   'host' : 'localhost'
# }
TOKEN_SECRET = os.environ.get('this is a small flask app that was developed super fast') or 'this is a small flask app that was developed super fast'
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
