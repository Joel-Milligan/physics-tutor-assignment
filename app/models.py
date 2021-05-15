import sqlalchemy
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String, Text
from  sqlalchemy.sql.expression import func, select
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(255)) # This is the hashed password
    description = db.Column(db.Text)
    signup_date = db.Column(db.DateTime, default=now())
    is_admin = db.Column(db.Boolean)

    def __init__(self, username: String, password: String, signup_date: DateTime, is_admin: Boolean) -> None:
        self.username = username
        self.set_password(password)
        self.signup_date = signup_date
        self.is_admin = is_admin

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Assessment(db.Model):
    id: Integer = db.Column(db.Integer, primary_key=True)
    question: Text = db.Column(db.Text)
    answer: Text = db.Column(db.Text)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self) -> str:
        return f'<Assessment {self.question}'

    def get_random_assessment(self):
        return select.order_by(func.rand())

class UserAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    completed = db.Column(db.Boolean)
    correct = db.Column(db.Boolean)

    def __init__(self, user_id, assessment_id, completed, correct):
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.completed = completed
        self.correct = correct

    def __repr__(self) -> str:
        return f'<UserAssessment {self.user_id}-{self.assessment_id}'