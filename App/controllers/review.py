from App.models import review
from App.database import db

def create_review(studentID, lecturerID):
    newreview = review()