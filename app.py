from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.dishes import dishes
from routes.restaurants import restaurants
from utils.conection import db
app = Flask(__name__)

app.secret_key = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://restaurant:password@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(dishes)
app.register_blueprint(restaurants)