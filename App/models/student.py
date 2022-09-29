from App.database import db

class student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    karmaScore = db.Column(db.Integer)

    def __init__(self, studentID, firstName, lastName, karmaScore):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.karmaScore = 0




