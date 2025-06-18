from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

class Student(db.Model, SerializerMixin):
    
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer())

    enrollments = relationship("Enrollment", back_populates="student")
    serialize_rules = ("-enrollments.student",)