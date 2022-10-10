from flask import Blueprint, render_template, jsonify, request, send_from_directory,redirect
from flask_jwt import jwt_required, current_identity


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
@jwt_required()
def add_Review():
    data=request.get_json()
    review=create_review(current_identity.id, data['studentID'], data['details'])
    if review==None:
        return jsonify("Error, Please enter valid Lecturer")
    return jsonify(review)

@review_views.route('/showAllReviews',methods=['GET'])
@jwt_required()
def showAllReviews():
    reviews=getAllReview_json()
    return jsonify(reviews)

@review_views.route('/showReview',methods=['GET'])
@jwt_required()
def displayReview():
    data=request.get_json()
    review=getReview(data['reviewID'])
    if review==None:
        return jsonify("Error, There is no review with that ID")
    review=review.toJSON()
    return jsonify(review)

@review_views.route('/updateReview/<reviewID>', methods=['PUT'])
@jwt_required()
def update(reviewID):
    data=request.get_json()
    result=updateReview(reviewID,data['details'])
    return jsonify(result)

@review_views.route('/deleteReview',methods=['DELETE'])
@jwt_required()
def remove():
    data=request.get_json()
    return deleteReview(data['reviewID'], data['studentID'])
     

@review_views.route('/rateReview', methods=['POST'])
@jwt_required()
def rate():
    data = request.get_json()
    return rateReview(data['reviewID'], data['studentID'],data['rating'])

