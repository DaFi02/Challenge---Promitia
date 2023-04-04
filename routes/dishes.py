from flask import Blueprint, jsonify, request, redirect, url_for, flash
from utils.conection import db

dishes = Blueprint('dishes', __name__)

@dishes.route('/dishes', methods=['GET'])
def get_dishes():
    return jsonify({'dishes': 'get_dishes'})