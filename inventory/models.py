# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'


import datetime
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    fb_id = db.Column(db.Integer, index=1)
    email = db.Column(db.String(100), nullable=1, unique=1)
    gender = db.Column(db.String(30), nullable=1)
    name = db.Column(db.String(50), nullable=1)

    nickname = db.Column(db.String(100), nullable=1)
    height = db.Column(db.Float, nullable=1, default=None)
    weight = db.Column(db.Float, nullable=1, default=None)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        self.created_at = self.updated_at = datetime.datetime.utcnow()
        self.updated_at = self.updated_at = datetime.datetime.utcnow()
        super(User, self).__init__(**kwargs)

    @classmethod
    def join_facebook(cls, **kwargs):
        user = cls.query.filter(cls.fb_id == kwargs.get(u'id')).first()
        if user:
            return user, 0

        data_dump = {
            'gender': kwargs.get(u'gender'),
            'email': kwargs.get(u'email'),
            'fb_id': kwargs.get(u'id'),
            'name': kwargs.get(u'name'),
        }

        new_user = cls(**data_dump)
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)

        return new_user, 1


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    name = db.Column(db.String(100), nullable=0, unique=1)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=1)

    parent = db.relationship('Category', backref=db.backref('sub_categories'), lazy='dynamic')

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    name = db.Column(db.String(100), nullable=0, unique=1)

    def __init__(self, **kwargs):
        super(Brand, self).__init__(**kwargs)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=0)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=0)
    name = db.Column(db.String(100), nullable=0)
    description = db.Column(db.Text, nullable=1)

    brand = db.relationship('Brand', backref=db.backref('items'), lazy='dynamic', cascade='all, delete-orphan')
    category = db.relationship('Category')

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)



