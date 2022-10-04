from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    authenticate,
    login_user
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/signup', methods=['POST','GET'])    
def signup():
    data = request.get_json()
    if data==None:
        data={
            "username": "vegeta",
            "firstName": "map",
            "lastName": "trump",
            "password": "waterbender"
        }
    result = create_user(data['username'],data['firstName'],data["lastName"],data['password'])
    
    if result:
        user=authenticate(data['username'],data['password'])
        #login_user(user)
        print(user)
        return jsonify({"message": "User created"}), 201
        #return render_template('index.html')
    return jsonify({"message": "Server error"}), 500

#@user_views.route('/users', methods=['GET'])
#def get_user_page():
#    users = get_all_users()
#    return jsonify(users)

@user_views.route('/api/users',methods=['GET'])
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')