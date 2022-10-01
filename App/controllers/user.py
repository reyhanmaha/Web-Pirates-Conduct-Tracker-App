from App.models import lecturer
from App.database import db

def create_user(username,firstName,lastName, password):
    newuser = lecturer(username=username, firstName=firstName, lastName=lastName, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return lecturer.query.filter_by(username=username).first()

def get_user(lecturerID):
    return lecturer.query.get(id)

def get_all_users():
    return lecturer.query.all()

def get_all_users_json():
    users = lecturer.query.all()
    #print(users)
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(lecturerID, username):
    user = get_user(lecturerID)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    