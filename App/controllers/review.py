from App.models import review
from App.database import db

def create_review(studentID, lecturerID, details):
    newreview = review(studentID, lecturerID, details)
    db.session.add(newreview)
    db.session.commit()
    return newreview
