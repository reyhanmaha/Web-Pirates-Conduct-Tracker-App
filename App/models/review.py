from App.database import db

class review(db.Model):
    reviewID = db.Column(db.Integer, primary_key=True)
    lecturerID = db.Column(db.Integer, primary_key=True)
    reviewID = db.Column(db.Integer, primary_key=True)
    reviewID = db.Column(db.Integer, primary_key=True)

    def __init__(self, studentID, firstName, lastName, up):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.upvote = 0
        self.downvotes = 0




