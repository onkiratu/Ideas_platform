from flask_sqlalchemy import SQLAlchemy
from my_app import db, migrate, login
from flask_login import UserMixin   

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(db.Model, UserMixin):
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True ) 
    firstname = db.Column(db.String(100), nullable=False )
    lastname = db.Column(db.String(100), nullable=False )   
    username = db.Column(db.String(100), nullable=False, unique=True )
    email = db.Column(db.String(100), nullable=False, unique=True )
    password = db.Column(db.String(50), nullable=False )

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True ) 
    type = db.Column(db.String(100), nullable=False )
    headline = db.Column(db.String(100), nullable=False )
    keywords = db.Column(db.String(100), nullable=False )
    description = db.Column(db.String(100), nullable=False )
    wordcount = db.Column(db.Integer, nullable=False )
    email = db.Column(db.String, nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey("payment.id"))


class Payment(db.Model):
    __tablename__ = "payment"
    id = db.Column(db.Integer, primary_key=True ) 
    payreference = db.Column(db.String(100), nullable=False, unique=True )
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))




