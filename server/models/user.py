from .database import db

class User(db.Model):

    __tablename__ = "users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),nullable=False)
    password=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String,nullable=False)


    def __repr__(self):
        return f"<User {self.username},{self.email}>"