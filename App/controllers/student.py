from App.models import student, review
from App.database import db

def create_student():
    pass


def getKarmaScore(studentID):

    upvotes = 0
    downvotes = 0

    reviews = review.query.all(studentID)

    for review in reviews:
        upvotes += review.upvotes
        downvotes += review.downvotes

    karma = upvotes - downvotes

    return karma

