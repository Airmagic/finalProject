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

    # https://stackoverflow.com/questions/24877025/runtimeerror-working-outside-of-application-context-when-unit-testing-with-py
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    # https://stackoverflow.com/questions/24877025/runtimeerror-working-outside-of-application-context-when-unit-testing-with-py
    # @classmethod
    # def setUpClass(cls)
    #     app.config['SERVER_NAME'] = 'localhost:5000'
    #     cls.client = app.test_client()

    # https://stackoverflow.com/questions/24877025/runtimeerror-working-outside-of-application-context-when-unit-testing-with-py
    def tearDown(self):
        self.app_context.pop()
    # def setUp(self):
    #     # TODO: Create temp db to use
    #     ItemsAPI.db = self.test_db_url
    #     basedir = os.path.abspath(os.path.dirname(__file__))
    #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'items.sqlite')
    #
    #
    #     db.session.commit()

    def test_add_item(self):
        # http://flask.pocoo.org/docs/1.0/appcontext/
        # with app.app_context():
        #     init_db()
        # https://stackoverflow.com/questions/31444036/runtimeerror-working-outside-of-application-context/31444175
        # with app.app_context():
        #     with patch('__main__.mysql.connector.connect') as  mock_mysql_connector_connect:
        #        object=TestMySQL()
        #        object.before_request() #Runtime error on calling this"""
        # TODO: make a test and comment out pass

        # r = self.post(url_for("item/add"))
        # self.assertEqual(r.status_code, 200)

        # item = ItemsAPI.Item("", "", "", "", "", "", "", "", "", "", "")
        # item = ItemsAPI.Item({"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""})
        # ItemsAPI.item_schema.jsonify(item)
        # expected = {"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""}
        # self.compare_db_expected(expected )
        # "cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""


        # c = app.test_client()
        # rv = c.get('/mypage', query_string={"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""})
        # expected_data = {"cost": "","itemName": "", "location": "", "user": "", "website": "", "whenBarrowed": "", "whenBought": "", "whenReturned": "", "whereBarrowed": "", "whereBought": "", "whoBarrowed": ""}
        # assert jsonify(rv.get_data()) == expected_data

        # gets
        # RuntimeError: Working outside of application context.
        #
        # This typically means that you attempted to use functionality that needed
        # to interface with the current application object in some way. To solve
        # this, set up an application context with app.app_context().  See the
        # documentation for more information.
        # pass

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


    # def compare_db_to_expected(self,expected):
    #     id = request.json['id']
    #     user =request.json['user']
    #     itemName = request.json['itemName']
    #     location = request.json['location']
    #     whereBought = request.json['whereBought']
    #     whenBought = request.json['whenBought']
    #     cost = request.json['cost']
    #     website = request.json['website']
    #     whoBarrowed = request.json['whoBarrowed']
    #     whenBarrowed = request.json['whenBarrowed']
    #     whenReturned = request.json['whenReturned']
    #     whereBarrowed = request.json['whereBarrowed']
        # Same rows in DB as entries in expected dictionary