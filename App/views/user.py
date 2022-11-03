from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    authenticate,
    login_user
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/signup', methods=['POST'])    
def signup():
    data = request.get_json()
    result = create_user(data['username'],data['firstName'],data["lastName"],data['password'])
    if result:
        return jsonify({"message": "User created"}), 201
    return jsonify({"message": "User is already created"}), 500

@user_views.route('/api/users',methods=['GET'])
@jwt_required()
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/identify')
@jwt_required()
def protected():
    return jsonify({'username':current_identity.username})

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')