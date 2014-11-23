# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'


import flask


bp = flask.Blueprint('main', __name__)


@bp.route('/')
def index():

    return flask.render_template('layout.html')
