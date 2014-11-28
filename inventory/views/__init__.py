# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'

from werkzeug.contrib.fixers import ProxyFix


def init_app(app):
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Blueprint 등록
    from . import main, auth, item
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(item.bp, url_prefix='/item')
