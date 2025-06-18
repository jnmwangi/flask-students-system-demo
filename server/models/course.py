from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    enrollments = relationship("Enrollment", back_populates="course")
    serialize_rules = ("-enrollments.course",)