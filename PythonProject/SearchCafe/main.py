import random

from flask import Flask, jsonify, render_template, request, redirect, url_for, json
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import func
from wtforms import StringField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DELETE_SECRET_KEY="1q2w3e4r"

db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __init__(self, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        tmp_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        cafe_list.append(tmp_dict)
    return jsonify(cafe_list)
    # return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    location = request.args.get('location')
    cafes = db.session.query(Cafe).filter_by(location=location).all()
    cafe_list = []

    for cafe in cafes:
        tmp_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        cafe_list.append(tmp_dict)
    return jsonify(cafe_list)


@app.route("/random")
def random_cafe():
    cafe = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(id=cafe.id,
                   name=cafe.name,
                   map_url=cafe.map_url,
                   img_url=cafe.img_url,
                   location=cafe.location,
                   seats=cafe.seats,
                   has_toilet=cafe.has_toilet,
                   has_wifi=cafe.has_wifi,
                   has_sockets=cafe.has_sockets,
                   can_take_calls=cafe.can_take_calls,
                   coffee_price=cafe.coffee_price)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    name = request.form['name']
    map_url = request.form['map_url']
    img_url = request.form['img_url']
    location = request.form['location']
    seats = request.form['seats']
    has_toilet = request.form['has_toilet']
    has_wifi = request.form['has_wifi']
    has_sockets = request.form['has_sockets']
    can_take_calls = request.form['can_take_calls']
    coffee_price = request.form['coffee_price']

    cafe_to_add = Cafe(name, map_url, img_url, location, seats, bool(has_toilet), bool(has_wifi), bool(has_sockets), bool(can_take_calls), coffee_price)

    with app.app_context():
        db.session.add(cafe_to_add)
        db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    new_price = request.form['new_price']
    cafe_to_update = db.session.query(Cafe).filter_by(id=cafe_id).first()

    if cafe_to_update is None:
        return jsonify({"error":{"Not found": "No cafe has been found."}})
    else:
        cafe_to_update.coffee_price = new_price
        with app.app_context():
            db.session.merge(cafe_to_update)
            db.session.commit()
        return jsonify(response={"success": "Successfully modified the new cafe."})


@app.route("/delete-cafe/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    delete_secret_key = request.form['DELETE_SECRET_KEY']
    cafe_to_delete = db.session.query(Cafe).filter_by(id=cafe_id).first()

    if cafe_to_delete is None:
        return jsonify({"error":{"Not found": "No cafe has been found."}})
    else:
        if delete_secret_key == DELETE_SECRET_KEY:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return jsonify({"error": {"Wrong secret key": "Provided secret key is wrong."}})




## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
