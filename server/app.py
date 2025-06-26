from flask import Flask, session, request
from models.database import db
from flask_migrate import Migrate
from controllers import controller
from dotenv import load_dotenv
from controllers import controller
from models import Student, Course, Enrollment, User
from flask_bcrypt import Bcrypt
from controllers.auth_controller import auth_bp
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import verify_jwt_in_request

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()
jwt = JWTManager()

db.init_app(app)
migration = Migrate(app, db)
bcrypt = Bcrypt(app)
CORS(app, origins=["http://localhost:5173"])
jwt.init_app(app)

protect_routes = [
    "/api/users",
    "/api/students",
    "/api/courses",
    "/api/enrollments"
]

# @app.before_request
# def isAuthenticated():
#     print(verify_jwt_in_request())
#     # current_user = get_jwt_identity()
#     # if not current_user and any( [ request.path.startswith(path) for path in protect_routes ] ):
#     #     return {"error":"Unauthorized"}, 403

@app.route("/", methods=["GET"])
def home():
    return "Nyumbani"


crud_routes = [
    { "name": "students", "model": Student },
    { "name": "courses", "model": Course },
    { "name": "enrollments", "model": Enrollment },
    { "name": "users", "model": User }
]

for route in crud_routes:
    students_bp = controller(**route)
    app.register_blueprint(students_bp, url_prefix=f'/api')


app.register_blueprint(auth_bp, url_prefix="/auth")

