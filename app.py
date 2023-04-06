from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.dishes import dishes
from routes.restaurants import restaurants
from utils.conection import db
app = Flask(__name__)

app.secret_key = 'e2c43954a7f94d259bf91820a8d6993a'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://challenge:123456@localhost/restaurants'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(dishes)
app.register_blueprint(restaurants)
