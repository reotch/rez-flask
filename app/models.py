from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    # first_name
    # last_name
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # phone_number
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'
    
class Education(db.Model):
    __tablename__ = "education"
    education_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key)