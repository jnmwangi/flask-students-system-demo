from flask_restful import Resource
from flask import request,jsonify
from models.database import db

class CoreController(Resource):

    def __init__(self, model):
        super().__init__()
        self.Model = model

    def get(self):
        # pagination
        # order
        # filters
        all = self.Model.query.all()

        return [item.to_dict() for item in all], 200
    
    def post(self):
        print("Add data")
        return "Added"
    
class CoreControllerOne(Resource):

    def __init__(self, model):
        super().__init__()
        self.Model = model

    def get(self, id):
        one = self.Model.query.filter_by(id=id).first()

        return one.to_dict(), 200
    
    def patch(self, id):
        one = self.Model.query.filter_by(id=id).first()
        data= request.get_json()
        for attr ,value in data.items():
            if hasattr(one, attr):
                setattr(one,attr, value)

        db.session.commit()
        return jsonify(one.to_dict())

        return "Patch"