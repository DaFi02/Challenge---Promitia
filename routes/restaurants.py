from flask import Blueprint, jsonify, request, redirect, url_for, flash
from utils.conection import db

restaurants = Blueprint('restaurants', __name__)

@restaurants.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify({'restaurants': 'get_restaurants'})

@restaurants.route('/restaurants/plato', methods=['GET'])
def create_dish():
    return jsonify({'restaurants': 'create_dish'})


