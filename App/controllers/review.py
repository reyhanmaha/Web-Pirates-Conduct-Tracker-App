from App.models import review, student, lecturer
from App.database import db
from App.controllers import create_student
from flask import jsonify

def create_review(lecturerID,studentID, details):
    data=student.query.get(studentID)
    user=lecturer.query.get(lecturerID)
    if user==None:
        return None
    if data==None:
        newStudent=create_student('gordon','barry',0)
        studentID=newStudent.studentID
    newReview = review(lecturerID=lecturerID,studentID=studentID,details=details)
    db.session.add(newReview)
    db.session.commit()
    return newReview.toJSON()

def getReview_json(reviewID):
    return review.query.filter_by(reviewID=reviewID).first().toJSON()

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

def deleteReview(reviewID):
    data=review.query.get(reviewID)
    if data==None:
        return jsonify("Error, No review found with this ID")
    db.session.delete(data)
    db.session.commit()
    return jsonify("Review has been deleted")