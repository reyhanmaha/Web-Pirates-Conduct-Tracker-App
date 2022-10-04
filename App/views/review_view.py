from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect
from flask_jwt import jwt_required


from App.controllers import (
    create_review, 
    getReview,
    getAllReview,
    getAllReview_json,
    getReview_json,
    deleteReview,
    rateReview,
    updateReview,
    calculateKarmaScore
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/createReview',methods=['POST'])
def add_Review():
    data=request.get_json()
    review=create_review(data['lecturerID'], data['studentID'], data['details'])
    if review==None:
        return jsonify("Error, Please enter valid Lecturer")
    return jsonify(review)

@review_views.route('/showAllReviews',methods=['GET'])
def showAllReviews():
    reviews=getAllReview_json()
    return jsonify(reviews)

@review_views.route('/showReview',methods=['GET'])
def displayReview():
    data=request.get_json()
    review=getReview_json(data['reviewID'])
    if review==None:
        return jsonify("Error, There is no review with that ID")
    return jsonify(review)

@review_views.route('/updateReview', methods=['POST'])
def update():
    data=request.get_json()
    result=updateReview(data['reviewID'],data['details'])
    return jsonify(result)

@review_views.route('/deleteReview',methods=['DELETE'])
def remove():
    data=request.get_json()
    return deleteReview(data['reviewID'])
     

@review_views.route('/rateReview', methods=['POST'])
def rate():
    data = request.get_json()
    return rateReview(data['reviewID'], data['studentID'],data['rating'])

