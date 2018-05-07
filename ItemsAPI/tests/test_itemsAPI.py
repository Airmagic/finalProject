# Python batteries included
from unittest import TestCase
import os

# importing itemsAPI program that Eric made
from ItemsAPI import add_item, get_item, item_detail, item_update, item_delete
import ItemsAPI


# These are pip installs
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, request, jsonify
app = Flask(__name__)
# Binding these to the Flask
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Making a class so the unit testing can use
class TestItemsAPI(TestCase):

    test_db_url = 'test_itemsAPI.db'


    def setUp(self):
        # TODO: Create temp db to use
        ItemsAPI.db = self.test_db_url
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'items.sqlite')


        db.session.commit()

    def test_add_item(self):
        # TODO: make a test and comment out pass
        item = ItemsAPI.Item("", "", "", "", "", "", "", "", "", "", "")
        # item = ItemsAPI.Item({"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""})
        # ItemsAPI.item_schema.jsonify(item)
        # expected = {"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""}
        # self.compare_db_expected(expected )
        # "cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""


        c = app.test_client()
        rv = c.get('/mypage', query_string={"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""})
        expected_data = {"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""}
        assert jsonify(rv.get_data()) == expected_data

        # gets
        # RuntimeError: Working outside of application context.
        #
        # This typically means that you attempted to use functionality that needed
        # to interface with the current application object in some way. To solve
        # this, set up an application context with app.app_context().  See the
        # documentation for more information.

    def test_get_item(self):
        # TODO: make a test and comment out pass
        pass

    def test_item_detail(self):
        # TODO: make a test and comment out pass
        pass

    def test_item_update(self):
        # TODO: make a test and comment out pass
        pass

    def test_item_delete(self):
        # TODO: make a test and comment out pass
        pass


    def compare_db_to_expected(self,expected):
        id = request.json['id']
        user =request.json['user']
        itemName = request.json['itemName']
        location = request.json['location']
        whereBought = request.json['whereBought']
        whenBought = request.json['whenBought']
        cost = request.json['cost']
        website = request.json['website']
        whoBarrowed = request.json['whoBarrowed']
        whenBarrowed = request.json['whenBarrowed']
        whenReturned = request.json['whenReturned']
        whereBarrowed = request.json['whereBarrowed']
        # Same rows in DB as entries in expected dictionary
