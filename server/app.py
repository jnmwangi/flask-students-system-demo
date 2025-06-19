from flask import Flask
from models.database import db
from flask_migrate import Migrate
from controllers import controller
from dotenv import load_dotenv
from models import Student, Course, Enrollment

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migration = Migrate(app, db)

@app.route("/", methods=["GET"])
def home():
    return "Nyumbani"

crud_routes = [
    { "name": "students", "model": Student },
    { "name": "courses", "model": Course },
    { "name": "enrollment", "model": Enrollment }
]

for route in crud_routes:
    students_bp = controller(**route)
    app.register_blueprint(students_bp, url_prefix=f'/{route["name"]}')


