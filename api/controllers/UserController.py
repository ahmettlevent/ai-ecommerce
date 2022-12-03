from flask_sqlalchemy import SQLAlchemy
from models.User import User
from flask import request
import jwt
import config
from forms.UserUpdateForm import UserUpdateForm


db = SQLAlchemy()


def index():
    token = jwt.decode(
        jwt=request.cookies.get("jwt"), key=config.SECRET_KEY, algorithms=["HS256"])

    user = User.query.filter_by(uid=token["uid"]).first()


    if user == None:
        return {"message": "Login or Register !"},400
    else:
        return user.serialize, 200

def update():
    token = jwt.decode(
        jwt=request.cookies.get("jwt"), key=config.SECRET_KEY, algorithms=["HS256"])

    data = request.get_json()
    form = UserUpdateForm(data=data)

    if not form.validate():
        return form.errors, 400

    user = User.query.filter_by(uid=token["uid"]).first()

    if user == None:
        return {"message": "User not found !"}, 401 

    user.name = form.name.data
    user.surname = form.surname.data
    user.city = form.city.data
    user.state = form.state.data
    user.address = form.address.data
    user.age = form.age.data

    db.session = db.session.object_session(user)
    db.session.commit()
    return {"message": "User was updated successfully"}, 200

def delete():
    token = jwt.decode(
        jwt=request.cookies.get("jwt"), key=config.SECRET_KEY, algorithms=["HS256"])

    user = User.query.filter_by(uid=token["uid"]).first()

    if user == None:
        return {"message": "Please register or login the account you want to delete !"},401


    try:
        db.session = db.session.object_session(user)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200    
    except:
        return {"message": "Database Error"}, 400
