from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column('id', db.Integer, primary_key=True)
    birth = db.Column('birth', db.Integer)
    gender = db.Column('gender', db.Text)

    responses = relationship("Responses", back_populates="user")

class Responses(db.Model):

    __tablename__ = "responses"

    id = db.Column('id', db.Integer, ForeignKey('user.id'), primary_key=True)
    understand = db.Column('understand', db.Integer)
    funny = db.Column('funny', db.Integer)
    frequent = db.Column('frequent', db.Integer)

class Questions(db.Model):

    __tablename__ = "questions"

    question_id = db.Column('question_id', db.Integer, primary_key=True)
    question = db.Column('question', db.Text)