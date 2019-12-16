from flask_login import UserMixin
from . import db

class Customers(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, unique=True)
    balance = db.Column(db.Float)
    password = db.Column(db.String(100))
