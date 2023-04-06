from utils.conection import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    dishes = db.relationship("Dish", back_populates="restaurant")
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type
        }        
    
    

class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    cost = db.Column(db.Float)
    price = db.Column(db.Float)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship("Restaurant", back_populates="dishes")

    def __init__(self, name, description, cost, price, restaurant_id):
        self.name = name
        self.description = description
        self.cost = cost
        self.price = price
        self.restaurant_id = restaurant_id
    
    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'cost': self.cost,
            'price': self.price,
            'restaurant_id': self.restaurant_id
        }