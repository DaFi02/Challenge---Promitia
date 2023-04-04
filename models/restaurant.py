from utils.conection import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    dishes = db.relationship("Dish", back_populates="restaurant")
    



class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    cost = db.Column(db.Float)
    price = db.Column(db.Float)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship("Restaurant", back_populates="dishes")
