# app.py - The main launch point
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return {'Welcome': 'Welcome to Hotel Booking APP'}


api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
