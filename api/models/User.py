from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(120))
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    age = db.Column(db.Integer)
    password = db.Column(db.String(120))

    @property
    def serialize(self):
        return {
            'name': self.name,
            "surname": self.surname,
            'email': self.email,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'age': self.age
        }

    def __init__(self, name, surname, email, city, state, address, age, password,):
        self.uid = uuid4(),
        self.name = name,
        self.surname = surname,
        self.email = email,
        self.city = city,
        self.state = state,
        self.address = address,
        self.age = age,
        self.password = generate_password_hash(password),

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
