from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollments"

    id = Column(Integer(), primary_key=True)
    student_id = Column(Integer(), ForeignKey("students.id", ondelete="CASCADE"))
    course_id = Column(Integer(), ForeignKey("courses.id", ondelete="CASCADE"))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    serialize_rules = ("-student.enrollments", "-course.enrollments")