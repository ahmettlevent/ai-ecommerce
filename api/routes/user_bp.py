from flask import Blueprint
from controllers.UserController import index, update, delete

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/update', methods=['POST'])(update)
user_bp.route('/delete', methods=['DELETE'])(delete)
