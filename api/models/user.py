from utils.db import db


class User(db.Model):
    __Table__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50),  nullable=False)
    lastname = db.Column(db.String(50),  nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(55), unique=True, nullable=False)
    account_number = db.Column(db.String(6), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)
