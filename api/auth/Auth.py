import jwt
from flask import Flask, jsonify, request


class Auth():
    def __init__(self, app) -> None:
        self.app = app

    def jwt_auht(self, blueprint_list):
        for blueprint in blueprint_list:
            @blueprint.before_request
            def wrapper():
                token = request.cookies.get("jwt")
                if not token:
                    return jsonify({"message": "Token is missing"}), 403
                try:
                    token = jwt.decode(
                        jwt=token, key=self.app.config["SECRET_KEY"], algorithms=["HS256"])
                except Exception:
                    return jsonify({"message": "Token is invalid!"}), 403
