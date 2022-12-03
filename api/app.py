from flask import Flask
from flask_migrate import Migrate
from auth.Auth import Auth
from models.User import db
from routes.user_bp import user_bp
from routes.auth_bp import auth_bp
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

cors = CORS(app, origins=["http://localhost:3000"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True,)

db.init_app(app)

migrate = Migrate(app, db)
auth = Auth(app)

auth.jwt_auht([user_bp])

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')



if __name__ == '__main__':
    app.run(host="localhost", port=8083)
