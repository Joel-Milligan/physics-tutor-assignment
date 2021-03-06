from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from app.models import User

def answer_integer(form, field: StringField):
    if not field.data.isdigit():
        raise ValidationError("Answer must be a whole number")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField('Admin Role?')
    submit = SubmitField('Register')

    # Check the username is not already taken
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class EditProfileForm(FlaskForm):
    description = StringField('Enter a new description')
    submit = SubmitField('Save')

class AnswerForm(FlaskForm):
    answer = StringField('Answer', validators=[DataRequired(), answer_integer])
    submit = SubmitField('Submit Answer')

class AddAssessmentForm(FlaskForm):
    question = StringField('Please submit a question', validators=[DataRequired()])
    answer = StringField('Please submit the answer', validators=[DataRequired(), answer_integer])
    submit = SubmitField('Create Assessment')