from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect
from flask_jwt import jwt_required


from App.controllers import (
    create_review, 
    getReview,
    getAllReview,
    getAllReview_json
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/createReview',methods=['POST'])
def add_Review():
    data=request.get_json()
    review=create_review(data['studentID'], data['lecturerID'], data['details'])
    return jsonify(review)

@review_views.route('/showAllReviews',methods=['GET'])
def showAllReviews():
    reviews=getAllReview_json()
    return jsonify(reviews)