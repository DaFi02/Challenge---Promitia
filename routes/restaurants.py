from flask import Blueprint, jsonify, request, session
from flask import current_app as app
from utils.conection import db
from models.restaurant import Restaurant
from flask_login import login_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from functools import wraps
import jwt


def check_token(func):
    @wraps(func)
    def authenticated(id, *args, **kwargs):
        token = session.get('token')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = Restaurant.query.filter_by(name=data['id']).first()
            if data['exp'] <= datetime.utcnow().timestamp():
                print(data['exp'], datetime.utcnow().timestamp())
                session.pop('token', None)
                session.pop('logged_in', None)
                return jsonify({'error': 'Token has expired!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token is invalid!'}), 401

        return func(id, current_user, *args, **kwargs)

    return authenticated

restaurants = Blueprint('restaurants', __name__)


@restaurants.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify({'restaurants': [restaurant.to_JSON() for restaurant in restaurants]})


@restaurants.route('/restaurants/<int:id>', methods=['GET'])
@check_token
def get_restaurant(id, current_user):
    
    restaurant = Restaurant.query.filter_by(id=id).first()
    if not restaurant:
        return jsonify({'message': 'Restaurant not found'}), 404
    return jsonify(restaurant.to_JSON())


@restaurants.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'message': 'Restaurant not found'}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return jsonify({'message': 'Restaurant deleted'})


@restaurants.route('/register', methods=['POST'])
def register():
    name = request.json['name']
    password = request.json['password']
    encrypted_password = generate_password_hash(password)
    new_restaurant = Restaurant(name, encrypted_password, "")

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify(new_restaurant.name)


@restaurants.route('/login', methods=['POST'])
def login():

    name = request.json['name']
    password = request.json['password']

    restaurant = Restaurant.query.filter_by(name=name).first()
    if restaurant is None:
        return jsonify({'message': 'Restaurant not found'}), 404

    # check_password
    if check_password_hash(restaurant.password, password):
        token = jwt.encode({
            'id': restaurant.name, 
            'exp': int((datetime.utcnow() + timedelta(minutes=6)).timestamp())}, app.config['SECRET_KEY'], algorithm='HS256')
        session['token'] = token
        return jsonify({'message': 'Restaurant login'}), 200

    return jsonify({'message': 'Password incorrect'})


@restaurants.route('/logout/<int:id>', methods=['POST'])
@check_token
def logout(id, current_user):
    session.pop('token', None)
    return jsonify({'user': 'logout'}), 200

@restaurants.route('/protected/<int:id>', methods=['GET'])
@check_token
def protected(id, current_user):
    return jsonify({'message': 'This is a protected route'}), 200

