# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'


import flask
from flask.ext.sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)
from . import models

from . import views
views.init_app(app)
