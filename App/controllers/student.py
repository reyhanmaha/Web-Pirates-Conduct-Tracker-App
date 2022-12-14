from App.models import student, review
from App.database import db

def create_student(firstName,lastName,karmaScore):
    pupil=student(firstName=firstName,lastName=lastName,karmaScore=karmaScore)
    db.session.add(pupil)
    db.session.commit()
    return pupil

def get_student_by_ID(studentID):
    return student.query.filter_by(studentID=studentID).first()

def get_student_by_ID_JSON(studentID):
    pupil=student.query.filter_by(studentID=studentID).first()
    return pupil.toJSON()

def get_all_students():
    return student.query.all()

def get_all_students_json():
    students = student.query.all()
    if not students:
        return []
    students = [student.toJSON() for student in students]
    return students

def updateStudent(studentID, firstName,lastName):
    data=student.query.get(studentID)
    if data==None:
        return "Error, There is no student with this ID"
    data.firstName=firstName
    data.lastName=lastName
    db.session.add(data)
    db.session.commit()
    return "Student data updated"
    

def deleteStudent(studentID):
    target=student.query.get(studentID)
    if target==None:
        return "Error, There is no student with this ID"
    db.session.delete(target)
    db.session.commit()
    return "Student Deleted"

#calls the calculateKarmaScore method in student model 

def calculateKarmaScore(studentID):
    data=review.query.filter_by(studentID=studentID).all()
    
    total = 0
    
    for value in data:
        total = total + value.upVotes
        total = total - value.downVotes
    pupil=student.query.get(studentID)
    pupil.karmaScore=total
    db.session.add(pupil)
    db.session.commit()
    return "Karma Score calculated"




