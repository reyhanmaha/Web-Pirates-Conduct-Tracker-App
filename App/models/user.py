from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class lecturer(db.Model):
    lecturerID = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(60), unique=True ,nullable=False)
    firstName= db.Column(db.String(50), nullable=False)
    lastName= db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120), unique=True , nullable=False)

    def __init__(self, username, firstName, lastName, password):
        self.username = username
        self.firstName=firstName
        self.lastName=lastName
        self.set_password(password)

    def toJSON(self):
        return{
            'lecturerID': self.lecturerID,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

