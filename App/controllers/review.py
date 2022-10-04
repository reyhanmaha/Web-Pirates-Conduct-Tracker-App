from App.models import review, student, lecturer
from App.database import db
from App.controllers import create_student
from flask import jsonify

def create_review(lecturerID,studentID, details):
    data=student.query.get(studentID)
    user=lecturer.query.get(lecturerID)
    if user==None:
        print(user)
        return jsonify("Error, Please enter valid Lecturer")
    if data==None:
        newStudent=create_student('gordon','barry',0)
        studentID=newStudent.studentID
    newReview = review(lecturerID=lecturerID,studentID=studentID,details=details)
    #print(newReview.lecturerID)
    db.session.add(newReview)
    db.session.commit()
    return newReview.toJSON()

def getReview(reviewID):
    return review.query.filter_by(reviewID=reviewID).first()

def getAllReview():
    return review.query.all()

def getAllReview_json():
    reviews = review.query.all()
    if not reviews:
        return []
    reviews = [review.toJSON() for review in reviews]
    return reviews