from App.models import review
from App.database import db

def create_review(studentID, lecturerID, details):
    newreview = review(studentID, lecturerID, details)
    db.session.add(newreview)
    db.session.commit()
    return newreview

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