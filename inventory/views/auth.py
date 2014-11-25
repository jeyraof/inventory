# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'


import flask
from ..helpers.oauth import facebook, FacebookProfileFetcher
from .. import models

bp = flask.Blueprint('auth', __name__)

FACEBOOK_TOKEN_KEY = 'facebook_oauth_token'


def login_as_user(user):
    flask.session['user_id'] = user.id


def logout_user():
    try:
        del flask.session['user_id']
    except KeyError:
        pass
    flask.g.user = None


@bp.before_app_request
def inject_user():
    user = flask.session.get('user_id')
    if user is not None:
        user = models.User.query.get(user)
    flask.g.user = user


@facebook.tokengetter
def get_facebook_oauth_token():
    return flask.session.get(FACEBOOK_TOKEN_KEY)


@bp.route('/facebook')
def facebook_login():
    if flask.g.user:
        return flask.redirect(flask.request.referrer or flask.url_for('main.index'))

    next_url = flask.request.args.get('next', flask.request.referrer) or None
    callback_url = flask.url_for('.facebook_oauth_authorized', next=next_url, _external=True)
    return facebook.authorize(callback=callback_url)


@bp.route('/facebook/oauth-authorized')
@facebook.authorized_handler
def facebook_oauth_authorized(resp):
    next_url = flask.request.args.get('next') or flask.url_for('main.index')
    if resp is None:
        return flask.redirect(next_url)

    flask.session[FACEBOOK_TOKEN_KEY] = (resp['access_token'], '')
    fetcher = FacebookProfileFetcher(resp.get('access_token', None),
                                     fields=['id', 'name', 'gender', 'email'])
    me = fetcher.fetch()
    user, created = models.User.join_facebook(**me.data)

    login_as_user(user)
    if created:
        flask.flash(u'회원 가입을 축하합니다!')

    return flask.redirect(next_url)


@bp.route('/logout')
def logout():
    logout_user()
    return flask.redirect(flask.url_for('main.index'))


@bp.route('/logged_in')
def logged_in():
    if flask.g.user:
        return flask.jsonify(ok=1, token=flask.g.user.token)
    return flask.jsonify(ok=0, token='')
