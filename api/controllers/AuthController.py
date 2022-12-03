from flask_sqlalchemy import SQLAlchemy
from flask import make_response
from models.User import User
from flask import request
import jwt
from forms.RegistrationForm import RegistrationForm
from forms.LoginForm import LoginForm
import datetime
from config import SECRET_KEY

db = SQLAlchemy()

def login():
    data = request.get_json()
    form = LoginForm(data=data)
    
    if not form.validate():
        return form.errors, 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return {"message": "User doesn't exist with that email. Please Register."}, 400

    if not user.verify_password(data["password"]):
        return {"message": "Wrong password."}, 400

    token = jwt.encode({"uid": user.uid, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)},
                       key=SECRET_KEY,
                       algorithm="HS256")
    response = make_response({"status": "success"})
    response.set_cookie("jwt", value=token)
    return response


def register():
    data = request.get_json()
    form = RegistrationForm(data=data)

    if not form.validate():
        return form.errors, 400

    if User.query.filter_by(email=data["email"]).first():
        return {"message": "A user already exist with that email. Please Login."}, 409

    user = User(
        name=data["name"],
        surname=data["surname"],
        email=data["email"],
        city=data["city"],
        state=data["state"],
        address=data["address"],
        age=data["age"],
        password=data["password"],
    )

    db.session.add(user)
    db.session.commit()

    token = jwt.encode({"uid": user.uid, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)},
                       key=SECRET_KEY,
                       algorithm="HS256")
    response = make_response({"message": "New user created !"})
    response.set_cookie("jwt", value= token)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")

    return response,201
