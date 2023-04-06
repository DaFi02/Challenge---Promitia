from flask import Blueprint, jsonify, request, redirect, url_for, flash
from utils.conection import db
from models.restaurant import Restaurant

restaurants = Blueprint('restaurants', __name__)

@restaurants.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify({'restaurants': [restaurant.to_JSON() for restaurant in restaurants]})


@restaurants.route('/restaurants', methods=['POST'])
def create_restaurant():
    name = request.json['name']
    type = request.json['type']
    new_restaurant = Restaurant(name, type)

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify(new_restaurant.name)



