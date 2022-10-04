from App.database import db
from .review import *

class student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    karmaScore = db.Column(db.Integer, nullable = True)
    studentComments= db.relationship('review',backref='student',lazy=True)

    def __init__(self, firstName, lastName,karmaScore):
        self.firstName = firstName
        self.lastName = lastName
        self.karmaScore = 0

    def toJSON(self):
        return{
            'studentID': self.studentID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'karmaScore': self.karmaScore
        }

    
