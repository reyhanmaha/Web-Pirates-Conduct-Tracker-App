from App.models import review, student
from App.database import db
from App.controllers import create_student

def create_review(lecturerID,studentID, details):
    data=student.query.get(studentID)
    if data==None:
        newStudent=create_student('gordon','barry',0)
        studentID=newStudent.studentID
    newReview = review(lecturerID,studentID, details)
    db.session.add(newReview)
    db.session.commit()
    return newReview

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