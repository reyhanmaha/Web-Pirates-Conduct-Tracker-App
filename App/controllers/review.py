from App.models import review, student, lecturer
from App.database import db
from App.controllers import create_student,calculateKarmaScore
from flask import jsonify

def create_review(id,studentID, details):
    data=student.query.get(studentID)
    user=lecturer.query.get(id)
    if user==None:
        return None
    if data==None:
        newStudent=create_student('gordon','barry',0)
        studentID=newStudent.studentID
    newReview = review(lecturerID=id,studentID=studentID,details=details)
    db.session.add(newReview)
    db.session.commit()
    return newReview.toJSON()

#returns just the review ID for every review the student is in
def get_student_reviews(studentID):

    student_reviews = review.query.filter_by(studentID=studentID).all()

    
    return [review.toJSON()['reviewID'] for review in student_reviews] 

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

def updateReview(reviewID,details):
    data = review.query.get(reviewID)
    if not data:
        return("Review doesnt exist")
    data.details = details
    db.session.add(data)
    db.session.commit()
    return("Review updated")

def deleteReview(reviewID, studentID):
    data=review.query.get(reviewID)
    if data==None:
        return jsonify("Error, No review found with this ID")
    db.session.delete(data)
    db.session.commit()
    calculateKarmaScore(studentID)  #calculate new karmaScore after review was deleted
    return jsonify("Review has been deleted")


def rateReview(reviewID, studentID, rating):
    data = review.query.get(reviewID)
    if data==None:
        return jsonify("The reviewID which you have entered does not exist")

    if rating !=1 and rating !=-1:
        return jsonify("Invalid rating number. Values are either 1 or -1")
    
    if rating==1:
        data.upVotes= data.upVotes + rating
        
    if rating==-1:
        data.downVotes= data.downVotes + 1
    db.session.add(data)
    db.session.commit()
    calculateKarmaScore(studentID)
    return jsonify("Rating successfully added.")