from App.models import student, review
from App.database import db

def create_student(firstName,lastName,karmaScore):
    pupil=student(firstName=firstName,lastName=lastName,karmaScore=karmaScore)
    db.session.add(pupil)
    db.session.commit()
    return pupil

def get_student_by_ID(studentID):
    return student.query.filter_by(studentID=studentID).first()

def get_all_students():
    return student.query.all()

def get_all_students_json():
    students = student.query.all()
    if not students:
        return []
    students = [student.toJSON() for student in students]
    return students

def getKarmaScore(studentID):

    upvotes = 0
    downvotes = 0

    reviews = review.query.all(studentID)

    for review in reviews:
        upvotes += review.upvotes
        downvotes += review.downvotes

    karma = upvotes - downvotes

    return karma

