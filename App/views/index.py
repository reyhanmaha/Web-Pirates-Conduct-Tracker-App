from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import lecturer
from App.controllers import *

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    #data=request.get_json()
    data={
        "username": "gale",
        "firstName": "yam",
        "lastName": "muck",
        "password": "larry"
    }
    #newUser=create_user(data["username"],data["firstName"],data["lastName"],data["password"])
    #print(newUser)
    #person=get_user_by_username(newUser.username)
    #print(person.toJSON())
    #people=get_all_users_json()
    #for person in people:
    #    print(person)
    return render_template('index.html')

#@index_views.route('/login', methods=['GET'])
#def login_user():
