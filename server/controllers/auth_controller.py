from flask_restful import Resource
from flask import request, Blueprint, session
from flask_restful import Api
from models import User
from flask_cors import CORS
from flask_jwt_extended import create_access_token

class AuthController(Resource):
    # from app import jwt

    def post(self):
        # content-type -> applicaiton/json
        
        jsondata = request.get_json()
        user = User.query.filter(User.email == jsondata["email"]).first()
        if not user:
            return {"error":"Invalid email adress"}, 403

        if not user.authenticate(jsondata["password"]):
            return {"error":"Invalid credentials"}, 403
        
        token = create_access_token(user.id)

        return {"access_token":token}
    
auth_bp = Blueprint("auth", __name__)
api = Api(auth_bp)

api.add_resource(AuthController, "/login")