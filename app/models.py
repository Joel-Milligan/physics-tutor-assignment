from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String, Text
from sqlalchemy.sql.expression import func
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
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

    def link_to_assessments(self):
        assessments: list[Assessment] = db.session.query(Assessment).all()
        for assessment in assessments:
            link = UserAssessment(self.id, assessment.id, False, False)
            db.session.add(link)
            
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        digest = md5(self.username.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

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

    def link_to_users(self):
        users: list[User] = User.query.all()
        for user in users:
            link = UserAssessment(user.id, self.id, False, False)
            db.session.add(link)

        db.session.commit()

    def get_new_assessment(user_id):
        # Get all uncompleted assessments that are linked to the user
        completed_assessments = db.session.query(Assessment).filter(
            User.id == user_id,
            UserAssessment.completed == False,
            UserAssessment.user_id == User.id, 
            UserAssessment.assessment_id == Assessment.id)

        # Get random assessment that hasn't been completed
        return completed_assessments.filter().order_by(func.random()).first()

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