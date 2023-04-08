from utils.conection import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True)
    password = db.Column(db.String(120))
    type = db.Column(db.String)
    
    dishes = db.relationship("Dish", back_populates="restaurant")
    
    def __init__(self, name, password, type):
        self.name = name
        self.password = password
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
    day = db.Column(db.String)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    
    restaurant = db.relationship("Restaurant", back_populates="dishes")

    def __init__(self, name, description, cost, price, day, restaurant_id):
        self.name = name
        self.description = description
        self.cost = cost
        self.price = price
        self.day = day
        self.restaurant_id = restaurant_id
    
    def to_JSON_to_resturant(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'cost': self.cost,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'day': self.day
        }
    
    def to_JSON_to_cliente(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'restaurant_id': self.restaurant_id
        }
