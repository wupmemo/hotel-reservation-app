# app.py - The main launch point
from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

# Init api
app = Flask(__name__)
# api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# Config Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)


# Hotel api Models
class HotelPackage(db.Model):
    pkg_num = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)
    duration = db.Column(db.Integer)
    pkg_duration = db.Column(db.Integer)
    description = db.Column(db.String(200))

    def __init__(self, hotel_name, price, duration, pkg_duration, description):
        self.hotel_name = hotel_name
        self.price = price
        self.duration = duration
        self.pkg_duration = pkg_duration
        self.description = description


# Hotel api Schema
class HotelPackageSchema(ma.Schema):
    class Meta:
        fields = ('pkg_num', 'hotel_name', 'price', 'duration', 'pkg_duration', 'description')


# Init api Schema
hotel_package_schema = HotelPackageSchema()
hotel_packages_schema = HotelPackageSchema(many=True)


# Setting up the API routes

# Root api endpoint
@app.route('/', methods=['GET', 'POST'])
def index():
    return {'Welcome': 'Welcome to Hotel Booking APP'}


# Create a new hotel package
@app.route('/package/new', methods=['POST'])
def new_package():
    app.logger.debug(hotel_package_schema)
    hotel_name = request.json['hotel_name']
    price = request.json['price']
    duration = request.json['duration']
    pkg_duration = request.json['pkg_duration']
    description = request.json['description']

    new_package = HotelPackage(hotel_name, price, duration, pkg_duration, description)
    db.session.add(new_package)
    db.session.commit()

    return hotel_package_schema.jsonify(new_package)


# Update a hotel package
@app.route('/package/update/<pkg_num>', methods=['PUT'])
def update_package():
    return {'update package': "pkg_num"}


# Update a hotel package
@app.route('/package/delete/<pkg_num>', methods=['PUT'])
def delete_package():
    return {'delete package': "pkg_num"}


# Show all current packages
@app.route('/package/list', methods=['GET'])
def get_all_packages():
    return {'packages': ["package1, package2, package3"]}


# Run Dev server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
