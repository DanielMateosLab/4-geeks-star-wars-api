"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# People endpoints
@app.route('/people')
def get_people():
    "Returns the list of people"
    people = [people.serialize() for people in People.query.all()]
    return jsonify(people), 200

@app.route('/people/<int:person_id>')
def get_person(person_id):
    "Returns person with id = person_id"
    person = People.query.get(person_id).serialize()
    return jsonify(person), 200

# Planet endpoints
@app.route('/planets')
def get_planets():
    "Returns the list of planets"
    planets = [planet.serialize() for planet in Planet.query.all()]
    return jsonify(planets), 200

@app.route('/planets/<int:planet_id>')
def get_planet(planet_id):
    "Returns planet with id = planet_id"
    planet = Planet.query.get(planet_id).serialize()
    return jsonify(planet), 200

# User endpoints
@app.route('/users', methods=['GET'])
def get_users():
    "Returns the list of users"
    users = [user.serialize() for user in User.query.all()]

    return jsonify(users), 200

@app.route('/users/<int:user_id>/favourites')
def get_favourites(user_id):
    "Returns favorites of user with id='user_id'"

@app.route('/users/<int:user_id>/favourites', methods=['POST'])
def add_favourite(user_id):
    """
    Adds favourite to user with 'user_id'
    Assumes a request body of shape: 
    {
        "type": "planet" | "people",
        "id": Int
    }
    """    
    pass

@app.route('/users/<int:user_id>/favourites/people/<int:person_id>', methods=['DELETE'])
def delete_person_favourite(user_id, person_id):
    "Deletes favorite person with id = person_id from user with id = user_id"
    pass

@app.route('/users/<int:user_id>/favourites/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favourite(user_id, planet_id):
    "Deletes favorite person with id = planet_id from user with id = user_id"
    pass

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
