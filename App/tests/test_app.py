import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import lecturer, student, review
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user,
    create_student,
    get_student_by_ID,
    updateStudent,
    deleteStudent,
    create_review,
    getReview,
    updateReview,
    deleteReview,
    rateReview,
    calculateKarmaScore,
    get_all_students_json,
    get_student_by_ID_JSON
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = lecturer('hawkings', "bob", "carl", "bobpass")
        assert user.username == "hawkings"

    def test_toJSON(self):
        user = lecturer('hawkings', "bob", "carl", "bobpass")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"hawkings", "firstName":"bob", "lastName":"carl"})
    
    def test_hashed_password(self):
        password = "bobpass"
        hashed = generate_password_hash(password, method='sha256')
        user = lecturer('hawkings', "bob", "carl", "bobpass")
        assert user.password != password

    def test_check_password(self):
        password = "bobpass"
        user = lecturer('hawkings', "bob", "carl", "bobpass")
        assert user.check_password(password)

    # Student Unit Tests

    def test_create_student(self):
        new_student = student("tim", "harold")
        assert new_student.karmaScore == 0


    def test_student_toJson(self):
        new_student = student("tim", "harold")
        new_student_JSON = new_student.toJSON()
        self.assertDictEqual({"studentID": None, "firstName":"tim", "lastName":"harold", "karmaScore":0}, new_student_JSON)


    #Review Unit Tests

    def test_create_review(self):
        new_review = review(1, 1, "very real data yep")
        assert new_review.reviewID == None

    def test_review_toJson(self):
        new_review = review(1, 1, "very real data yep")
        new_review_JSON = new_review.toJSON()
        self.assertDictEqual({"reviewID": None, "lecturerID":1, "studentID":1,
                             "details":"very real data yep", "upVotes":0, "downVotes": 0}, new_review_JSON)


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bobby1","bob", "bobson","bobpass")
    assert authenticate("bobby1", "bobpass") != None





class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "rick", "ricky", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual(users_json, [{"id":1, "username":"bobby1", "firstName" : "bob", "lastName" : "bobson"},
                                          {"id":2, "username":"rick", "firstName": "rick", "lastName" : "ricky"}])

    def test_update_user(self):
        test = update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
        
    def test_get_user(self):
        user=get_user(1)
        assert user !=None
    
    def test_create_student(self):
        student= create_student("tim","morgan",4)
        assert student.firstName=="tim"
    
    def test_get_student_by_ID(self):
        student=get_student_by_ID(1)
        assert student!=None
    
    def test_updateStudent(self):
        student=get_student_by_ID(1)
        updateStudent(1,"dwayne","johnson")
        person=get_student_by_ID(1)
        assert person.firstName=="dwayne"
    
    def test_deleteStudent(self):
        student=create_student("morgan", "freeman", 10)
        create_student("terry", "silver", 3)
        deleteStudent(2)
        person=get_student_by_ID(2)
        print(person)
        assert person==None
    
    def test_create_review(self):
        review=create_review(1,1,"bad student")
        item=getReview(1)
        assert item!=None
    
    def test_updateReview(self):
        updateReview(1,"very good student")
        review=getReview(1)
        assert review.details=="very good student"
    
    def test_deleteReview(self):
        review=create_review(1, 1, "he falls asleep in class")
        deleteReview(2,1)
        item=getReview(2)
        assert item==None
    
    def test_rateReview(self):
        rateReview(1,1,-1)
        student=get_student_by_ID(1)
        assert student.karmaScore==-1

    def test_calculateKarmaScore(self):
        pass
    