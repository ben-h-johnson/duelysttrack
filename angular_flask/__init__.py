import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager


app = Flask(__name__)
db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)
lm = LoginManager()
lm.init_app(app)
app.config.from_object('angular_flask.settings')

app.url_map.strict_slashes = False

import angular_flask.models
import angular_flask.views
