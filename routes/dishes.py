from flask import Blueprint, jsonify, request, redirect, url_for, flash
from utils.conection import db
from models.restaurant import Dish

dishes = Blueprint('dishes', __name__)

@dishes.route('/dishes', methods=['GET'])
def get_dishes():
    
    return jsonify({'dishes': 'get_dishes'})


@dishes.route('/dishes', methods=['POST'])
def add_dish():
    name = request.json['name']
    description = request.json['description']
    cost = request.json['cost']
    price = request.json['price']
    restaurant_id = request.json['restaurant_id']
    new_dish = Dish(name, description, cost, price, restaurant_id)

    db.session.add(new_dish)
    db.session.commit()

    return jsonify(new_dish.name)

