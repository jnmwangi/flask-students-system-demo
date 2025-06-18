from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin


class Gender(db.Model):
    __tablename__ = "gender"

    id = Column(Integer(), primary_key=True)
    name = Column(String())