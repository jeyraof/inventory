# -*- coding: utf-8 -*-

import flask
from .. import models

bp = flask.Blueprint('item', __name__)


@bp.route('/<int:item_id>')
def item_detail(item_id):
    pass


@bp.route('/new', methods=['POST', 'GET'])
def new_item():
    valid, string = models.Item.validate_new(form=flask.request.form)
    if not valid:
        return flask.jsonify(ok=0, msg=string)

    category = models.Category.query.get(flask.request.form.get('category_id'))
    if not category:
        return flask.jsonify(ok=0, msg=u'잘못된 카테고리를 선택하셨습니다.')

    brand = models.Brand.query.get(flask.request.form.get('brand_id'))
    if not brand:
        return flask.jsonify(ok=0, msg=u'잘못된 브랜드를 선택하셨습니다.')

    created_item = models.Item.create(brand=brand, category=category,
                                      name=flask.request.form.get('name'),
                                      description=flask.request.form.get('description'))
    return flask.jsonify(ok=1, item_id=created_item.id)


@bp.route('/get_brands')
def get_brands():
    """
    :argument keyword
    :return list of brands containing keyword
    """
    keyword = flask.request.args.get('keyword', '')
    brands = models.Brand.query
    if keyword:
        brands.filter(models.Brand.name.like('%%%s%%' % keyword))
    brands = sort_by_name([{'id': x.id, 'name': x.name} for x in brands.all()])
    return flask.jsonify(brands=brands)


@bp.route('/get_categories')
def get_categories():
    """
    :return: list of categories
    """
    categories = sort_by_name([{'id': x.id, 'name': x.name} for x in models.Category.query.all()])
    return flask.jsonify(categories=categories)


def sort_by_name(a):
    return sorted(a, key=lambda y: y['name'])