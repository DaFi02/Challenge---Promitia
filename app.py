from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.conection import db
app = Flask(__name__)

app.secret_key = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://restaurant:123456@password/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False