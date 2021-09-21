from operator import index
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), unique = True,index = True)
    order = db.Column(db.String(255), index = True)

    def __repr__(self):
        return f'User {self.username}'

class Restaurant(db.Model):
    __tablename__ = 'rests'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), unique = True, index = True)
    food = db.Column(db.String(255), index = True)
    location = db.Column(db.String(255), index = True)

    def __repr__(self):
        return f'Restaurant {self.name}'

class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), index = True)
    price = db.Column(db.Integer, index = True)
    crust = db.Column(db.String(255), index = True)

    def __repr__(self):
        return f'Food {self.name}'

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),index = True)
    Content = db.Column(db.String(255),index = True)

    def __repr__(self):
        return f'Review {self.title}'

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer,primary_key = True)
    food_order = db.Column(db.String(255),index = True)
    amount = db.Column(db.Integer,index = True)

    def __repr__(self):
        return f'Order {self.food_order}'

class Delivery(db.Model):
    __tablename__ = 'delivery'

    id = db.Column(db.Integer,primary_key = True)
    food = db.Column(db.String(255),index = True)
    place = db.Column(db.String(255),index = True)
    charges = db.Column(db.String(40),index = True)

    def __repr__(self):
        return f'Delivery {self.food}'

