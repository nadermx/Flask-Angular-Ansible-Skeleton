# -*- coding: utf-8 -*-
# Import flask and template operators
from flask import Flask, render_template


# Import PonyOrm
from app import models

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# set a global db session for the app
app.wsgi_app = models.db_session(app.wsgi_app)

# Pony ORM database config
# Build the database:
# This will create the database file using PonyOrm
models.db.bind(app.config['DB_PROVIDER'], **app.config['DB_CONFIG'])
models.db.generate_mapping(create_tables=True)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (web)
from app.frontend.views import mod as frontend_module
# Register blueprint
app.register_blueprint(frontend_module)

