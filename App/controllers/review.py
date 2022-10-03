from App.models import review
from App.database import db

def create_review(studentID, lecturerID, details):
    newReview = review(studentID, lecturerID, details)
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