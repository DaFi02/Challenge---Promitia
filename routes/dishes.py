from flask import Blueprint, jsonify, request, redirect, url_for, flash
from utils.conection import db
from models.restaurant import Dish, Restaurant
from datetime import datetime

dishes = Blueprint('dishes', __name__)

buy = []

#Lista todos los platos de todos los restaurantes
#quiza lo borre
@dishes.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.query.all()
    return jsonify({'dishes': [dish.to_JSON_to_resturant() for dish in dishes]})


#Lista todos los platos de un restaurante por el lado del cliente
@dishes.route('/dishes/<restaurant_id>/client', methods=['GET'])
def get_dishes_client(restaurant_id):
    day = datetime.now().strftime("%A")
    day = str.lower(day)
    dishes = Dish.query.filter_by(day=day, restaurant_id=restaurant_id)
    name_restaurant = Restaurant.query.filter_by(id=restaurant_id).first().name
    return jsonify({'dishes'+ " of "+name_restaurant : [dish.to_JSON_to_cliente() for dish in dishes]})

#Añade un plato a un restaurante
@dishes.route('/dishes', methods=['POST'])
def add_dish():
    name = request.json['name']
    description = request.json['description']
    cost = request.json['cost']
    price = request.json['price']
    day = str.lower(request.json['day'])
    restaurant_id = request.json['restaurant_id']
    new_dish = Dish(name, description, cost, price, day, restaurant_id)

    db.session.add(new_dish)
    db.session.commit()

    return jsonify(new_dish.name)

#Lista todos los platos de un restaurante
@dishes.route('/dishes/<int:restaurant_id>', methods=['GET'])
def get_dish_of_restaurant(restaurant_id):
    dish = Dish.query.filter_by(restaurant_id=restaurant_id)
    if not dish:
        return jsonify({'message': 'Dish not found'}), 404
    
    return jsonify({'dishes': [dish.to_JSON_to_resturant() for dish in dish]})

#Actualiza un plato de un restaurante
@dishes.route('/dishes/<restaurant_id>/<int:dish_id>', methods=['PUT'])
def update_dish(restaurant_id, dish_id):
    dish = Dish.query.filter_by(id=dish_id, restaurant_id=restaurant_id).first()
    if not dish:
        return jsonify({'message': 'Dish not found'}), 404
    
    dish.name = request.json['name']
    dish.description = request.json['description']
    dish.cost = request.json['cost']
    dish.price = request.json['price']
    dish.day = str.lower(request.json['day'])
    dish.restaurant_id = request.json['restaurant_id']

    db.session.commit()

    return jsonify({'message': 'Dish updated'})

#Elimina un plato de un restaurante
@dishes.route('/dishes/<restaurant_id>/<int:dish_id>', methods=['DELETE'])
def delete_dish(restaurant_id, dish_id):
    dish = Dish.query.filter_by(id=dish_id, restaurant_id=restaurant_id).first()
    if not dish:
        return jsonify({'message': 'Dish not found'}), 404
    
    db.session.delete(dish)
    db.session.commit()

    return jsonify({'message': 'Dish deleted'})

#Añade un plato a la compra
@dishes.route('/dishes/<int:restaurant_id>/<int:dish_id>/buy', methods=['POST'])
def add_dish_to_buy(restaurant_id, dish_id):
    dish = Dish.query.filter_by(id=dish_id, restaurant_id=restaurant_id).first()
    if not dish:
        return jsonify({'message': 'Dish not found'}), 404
    
    buy.append(dish.to_JSON_to_cliente())

    return jsonify({'message': 'Dish added', 'dish': buy})

@dishes.route('/dishes/buy', methods=['GET'])
def close_buy():
    
    close_buy = buy
    buy = []
    
    return jsonify({'message': 'Buy closed', 'dish': close_buy})