from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect
from flask_jwt import jwt_required


from App.controllers import (
    create_student, 
    get_student_by_ID,
    get_all_students,
    get_all_students_json,
    getKarmaScore
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/addStudent', methods=['POST'])
#@jwt_required()
def add_student():
    data=request.get_json()
    student=create_student(data['firstName'], data['lastName'],0)
    return jsonify(student)

@student_views.route('/showStudents', methods=['GET'])
#@jwt_required()
def show_all_students():
    students=get_all_students_json()
    return students

@student_views.route('/getStudent/<studentID>',methods=['GET'])
@jwt_required()
def find_student(studentID):
    target=get_student_by_ID(studentID)
    return target.toJSON()