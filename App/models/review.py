from App.database import db

class review(db.Model):
    reviewID = db.Column(db.Integer, primary_key=True)
    lecturerID= db.Column(db.Integer,db.ForeignKey('lecturer.lecturerID'), nullable=False)
    studentID= db.Column(db.Integer,db.ForeignKey('student.studentID'), nullable=False)
    details = db.Column(db.String(120), primary_key=True)
    upVotes = db.Column(db.Integer, nullable = True)
    downVotes = db.Column(db.Integer, nullable = True)

    
    def __init__(self, reviewID, lectureID, studentID, details ):
        self.reviewID= reviewID
        self.lectureID = lectureID
        self.studentID = studentID
        self.details = details
        self.upVotes = 0
        self.downVotes = 0

    def toJSON(self):
        return{
            'reviewID': self.reviewID,
            'lectureID': self.lectureID,
            'studentID': self.studentID,
            'details' :self.details,
            'upVotes': self.upVotes,
            'downVotes' : self.downVotes
        }



