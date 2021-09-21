from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String,index = True)
    email = db.Column(db.String, unique = True,index = True)
    order = db.Column(db.String, index = True)

    def __repr__(self):
        return f'User {self.username}'

class Restauraunt(db.Model):
    __tablename__ = 'rests'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String, unique = True, index = True)
    food = db.Column(db.String, index = True)
    location = db.Column(db.String, index = True)

    def __repr__(self):
        return f'Restaurant {self.name}'




class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String, index = True)
    price = db.Column(db.Integer, index = True)
    crust = db.Columnn(db.Integer, index = True)

    def __repr__(self):
        return f'Food {self.name}'
