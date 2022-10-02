from App.models import lecturer, student, review
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
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def create_review(studentID, lecturerID, details):

    student = student.query(studentID)

    if not student:
        newStudent = student(firstName="update", lastName ="me")
        db.session.add(newStudent)
        db.session.commit() # not sure if needed
        studentID = newStudent.studentID
        
    newreview = review(studentID, lecturerID, details)
    db.session.add(newreview)
    db.session.commit()
    return newreview

def update_review(reviewID, lecturerID, details):
    pass

#not sure if functions would require readded and commiting reviews to model

def rate_revew(reviewID, rate):
    
    review = review.query(reviewID)

    if not review:
        return("Review doesnt exist")

    if rate > 0:
        review.upvotes += 1
    else:
        review.downvotes += 1

    return ("rated")

def delete_review(reviewID):
    pass

def edit_review(reviewID, details):

    review = review.query(reviewID)

    if not review:
        return("Review doesnt exist")
    
    review.details = details

    return("Review updated")

def view_review(reviewID):

    return(review.query(reviewID))

def view_all_reviews():
    return(review.query.all())



def update_user(lecturerID, username):
    user = get_user(lecturerID)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    