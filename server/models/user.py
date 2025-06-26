from .database import db
from sqlalchemy.ext import hybrid
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),nullable=False)
    __password=db.Column(db.String(),nullable=False)
    email=db.Column(db.String,nullable=False)

    serization_rul=("-__password", "-_User__password")

    def __repr__(self):
        return f"<User {self.username},{self.email}>"
    
    @hybrid.hybrid_property
    def password(self):
        return ""
    
    @password.setter
    def password(self, plain_text):
        # Validation for strong password
        from app import bcrypt
        password_hash = bcrypt.generate_password_hash(plain_text.encode("utf-8"))
        self.__password = password_hash.decode("utf-8")

    def authenticate(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self.__password, password.encode("utf-8"))