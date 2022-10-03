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

#calls the calculateKarmaScore method in student model 
def getKarmaScore(studentID):
    value = calculateKarmaScore(studentID)
    return jsonify(value)



