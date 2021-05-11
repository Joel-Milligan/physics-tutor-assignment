import sqlalchemy
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String
from app import db 

class User(db.Model):
    id: Integer = db.Column(db.Integer, primary_key=True)
    username: String = db.Column(db.String(255), index=True, unique=True)
    password: String = db.Column(db.String(255)) # TODO: Hashing
    description: String = db.Column(db.Text)
    signup_date: DateTime = db.Column(db.DateTime, default=now())
    is_admin: Boolean = db.Column(db.Boolean)

    def __init__(self, username: String, password: String, description: String, signup_date: DateTime, is_admin: Boolean) -> None:
        self.username = username
        self.password = password
        self.description = description
        self.signup_date = signup_date
        self.is_admin = is_admin

    def __repr__(self):
        return f'<User {self.username}>'

# TODO: Assessment and UserAssessment Tables