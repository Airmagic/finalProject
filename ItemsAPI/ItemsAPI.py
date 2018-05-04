# The base of this code comes from
# https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

# Importing flask request and jsonify from flask pipinstall
from flask import Flask, request, jsonify
# pip install
from flask_sqlalchemy import SQLAlchemy
# pip install
from flask_marshmallow import Marshmallow
# Python battery included
import os

# Making the variable flask
app = Flask(__name__)

# This part create an instances of our web application and set path of our SQLite uri.
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'items.sqlite')

# Binding these to the Flask
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Declaring the model
class Item(db.Model):

    def __init__(self, user, itemName, location, whereBought, whenBought, cost, website, whoBarrowed, whenBarrowed, whenReturned, whereBarrowed):
        self.user = user
        self.itemName = itemName
        self.location = location
        self.whereBought = whereBought
        self.whenBought = whenBought
        self.cost = cost
        self.website = website
        self.whoBarrowed = whoBarrowed
        self.whenBarrowed = whenBarrowed
        self.whenReturned = whenReturned
        self.whereBarrowed = whereBarrowed

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=False)
    itemName = db.Column(db.String(120), unique=False)
    location = db.Column(db.String(120), unique=False)
    whereBought = db.Column(db.String(120), unique=False)
    whenBought = db.Column(db.String(120), unique=False)
    cost = db.Column(db.String(120), unique=False)
    website = db.Column(db.String(200), unique=False)
    whoBarrowed = db.Column(db.String(80), unique=False)
    whenBarrowed = db.Column(db.String(120), unique=False)
    whenReturned = db.Column(db.String(120), unique=False)
    whereBarrowed = db.Column(db.String(120), unique=False)

# define that JSON response will have these keys
class ItemSchema(ma.Schema):
    class Meta:
        #fields that are expose
        fields = ('id', 'user', 'itemName', 'location', 'whereBought', 'whenBought', 'cost', 'website', 'whoBarrowed', 'whenBarrowed', 'whenReturned', 'whereBarrowed')

class ItemsListSchema(ma.Schema):
    class Meta:
        #fields that are expose
        fields = ('itemName', 'location')

# definning the instances of item schemas
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
itemList_schema = ItemsListSchema()
itemsList_schema = ItemsListSchema(many=True)

#defines Endpoint to create new items
@app.route("/item/add", methods=["POST"])

# define function that will executed if we access this endpoint
def add_item():
    user = request.json['user']
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

    # Creating a new item from the model
    new_item = Item(user, itemName, location, whereBought, whenBought, cost, website, whoBarrowed, whenBarrowed, whenReturned, whereBarrowed)

    # adding the object to the db
    db.session.add(new_item)
    db.session.commit()

    return item_schema.jsonify(new_item)

# endpoint to show all items
@app.route("/items", methods=["GET"])
# function to get all the items for the list
def get_item():
    all_items = Item.query.all()
    result = items_schema.dump(all_items)
    return jsonify(result.data)

# endpoint to get item detail by id
@app.route("/item/<id>", methods=["GET"])
# function to get one item
def item_detail(id):
    # making a variable that is the item by id coming from the db
    item = Item.query.get(id)
    return item_schema.jsonify(item)

# endpoint to update item from id
@app.route("/item/update", methods=["PUT"])
def item_update(id):
    # Filling in the fields with the items information
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

    # setting the objects variables based on the changes
    item.user = user
    item.itemName = itemName
    item.location = location
    item.whereBought = whereBought
    item.whenBought = whenBought
    item.cost = cost
    item.website = website
    item.whoBarrowed = whoBarrowed
    item.whenBarrowed = whenBarrowed
    item.whenReturned = whenReturned
    item.whereBarrowed = whereBarrowed

    # commiting to the db
    db.session.commit()
    return item_schema.jsonify(user)

# endpoint to delete item
@app.route("/item/delete", methods=["DELETE"])
# function to delete item from db
def item_delete(id):
    # creating a variable from the db by id
    item = Item.query.get(id)
    if item != null:
        # telling the db to delete item
        db.session.delete(item)
        db.session.commit()
    else:
        return item_schema.jsonify(item)

    return item_schema.jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
