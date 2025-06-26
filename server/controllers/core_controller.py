from flask_restful import Resource
from flask import request,jsonify
from models.database import db
from flask_jwt_extended import jwt_required

class CoreController(Resource):

    def __init__(self, model):
        super().__init__()
        self.Model = model
    
    @jwt_required()
    def get(self):
        # pagination
        # order
        # filters
        all = self.Model.query.all()

        return jsonify({"data":[item.to_dict() for item in all]}), 200
    
    @jwt_required()
    def post(self):
        print("Add data")
        return {"error":"error"}

class CoreControllerOne(Resource):

    def __init__(self, model):
        super().__init__()
        self.Model = model

    @jwt_required()
    def get(self, id):
        one = self.Model.query.filter_by(id=id).first()

        return jsonify({"data":one.to_dict()}), 200
    
    @jwt_required()
    def patch(self, id):
        one = self.Model.query.filter_by(id=id).first()
        data= request.get_json()
        for attr ,value in data.items():
            if hasattr(one, attr):
                setattr(one,attr, value)

        db.session.commit()
        return jsonify({"data":one.to_dict()})