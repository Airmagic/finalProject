from unittest import TestCase
import os

# importing itemsAPI program that Eric made
from ItemsAPI import Item, add_item, get_item, item_detail, item_update, item_delete
import ItemsAPI

# These are pip installs
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, request, jsonify

import tempfile
import flask

from ItemsAPI import app   # import YOUR app, don't make a new one
db = SQLAlchemy(app)
ma = Marshmallow(app)

class TestItemsAPI(TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        test_db_url = 'test_itemsAPI.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, test_db_url)
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

        db.drop_all()
        db.create_all()

        # Just do setup here, no assertions.

    # no homepage so a 404 error is expected
    def test_get_items_returns_empty_dictionary(self):
        resp = self.app.get('/items')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, {})


    def test_post_to_add_item_adds_new_item_to_db(self):
        resp = self.app.post('/item/add', data=dict(user='me', itemName="screwdriver"))
        expected_item = Item('me', 'screwdriver')
        self.assertEqual(resp.status_code, 201)  # send 201 for created
        # Check DB
        all_items = Item.query.all()
        self.assertEqual(len(all_items), 1)
        self.assertEqual(all_items[0], expected_item)


class TestItemsAPIWithInitialData(TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        test_db_url = 'test_itemsAPI.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, test_db_url)
        app.config['TESTING'] = True
        self.app = app.test_client()

        db.drop_all()
        db.create_all()

        # Item(user, itemName, location, whereBought, whenBought, cost, website, whoBarrowed, whenBarrowed, whenReturned, whereBarrowed):

        item1 = Item('me', 'tool', 'myhouse1', 'stuff', 'whatever', 'a', 'b', 'c', 'd', 'e', 'f')
        item2 = Item('me2', 'tool2', 'my house2', 'stuff2', 'whatever2', 'a2', 'b2', 'c2', 'd2', 'e2', 'f')
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

        self.initial_test_items = [item1, item2]


    # no homepage so a 404 error is expected
    def test_get_items_returns_two_test_items(self):
        resp = self.app.get('/items')
        self.assertEqual(resp.status_code, 200)
        self.assertCountEqual(resp.data, self.initial_test_items)  # Same things in the list


if __name__ == '__main__':
    TestCase.main()
