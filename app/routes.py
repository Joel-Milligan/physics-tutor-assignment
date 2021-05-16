from datetime import datetime
from flask import render_template, flash, redirect, request
from flask.helpers import url_for
from flask_login import current_user, login_user, login_required
from flask_login.utils import logout_user
from werkzeug.urls import url_parse
from app import app, db
from app.forms import AnswerForm, LoginForm, RegisterForm, AddAssessmentForm, EditProfileForm
from app.models import User, Assessment, UserAssessment

@app.route('/')
@login_required
def index():
    return render_template('HomePage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Setup login form
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    # Setup registration form
    register_form = RegisterForm()

    return render_template('LoginRegisterPage.html', login_form=login_form, register_form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    flash("Successfully logged out.")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return redirect(url_for('login'))
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # Setup registration form
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = User(
            username=register_form.username.data, 
            password=register_form.password.data, 
            is_admin=register_form.is_admin.data, 
            signup_date=datetime.now())

        db.session.add(user)
        user.link_to_assessments()
        db.session.commit()
        flash(f"Successfully registered user: {user.username}")
    else:
        flash("Could not register user")
        
    return redirect(url_for('login'))

@app.route('/assessment-navigator')
@login_required
def navigate():
    return render_template('AssessmentNavigator.html')

@app.route('/assessment', methods=['GET','POST'])
@login_required
def assessment():
    assessment: Assessment = Assessment.get_new_assessment(current_user.id)
    
    if assessment is None:
        flash("No more assessments!")
        return redirect(url_for('index' ))

    userAssessment: UserAssessment = UserAssessment.query.filter_by(user_id=current_user.id, assessment_id=assessment.id).first()
    answer_form = AnswerForm()

    if answer_form.validate_on_submit():
        if answer_form.answer.data == assessment.answer:
            flash("Correct!")
            userAssessment.completed = True
            userAssessment.correct = True
        else:
            flash("Incorrect!")
            userAssessment.completed = True
            userAssessment.correct = False

        db.session.commit()
        return redirect(url_for('assessment'))

    return render_template('AssessmentPage.html', assessment=assessment, answer_form=answer_form)

@app.route('/profile')
@login_required
def profile():
    num_assessments_completed  = UserAssessment.query.filter_by(user_id = current_user.id, completed = True).count()
    num_assessments_correct = UserAssessment.query.filter_by(user_id = current_user.id, completed = True, correct = True).count()

    if(num_assessments_completed == 0):
        percent_correct = 0
    else:
        percent_correct = num_assessments_correct / num_assessments_completed

    return render_template('ProfilePage.html', num_assessments_completed =num_assessments_completed, num_assessments_correct = num_assessments_correct, percent_correct = percent_correct)

@app.route('/description', methods=['GET', 'POST'])
@login_required
def description():
    description_form = EditProfileForm()

    if description_form.validate_on_submit():
        current_user.description = description_form.description.data
        db.session.commit()
        return redirect(url_for('profile'))
        
    return render_template('EditDescription.html', description_form=description_form, old_description=current_user.description)

@app.route('/content')
@login_required
def content():
    return render_template('TeachingPage.html')

@app.route('/create-assessment', methods=['GET', 'POST'])
@login_required
def addAssessment():
    if not current_user.is_admin:
        return redirect(url_for('index'))

    assessment_form = AddAssessmentForm()

    if assessment_form.validate_on_submit():
        assessment = Assessment(
            question=assessment_form.question.data, 
            answer=assessment_form.answer.data)

        db.session.add(assessment)
        assessment.link_to_users()
        db.session.commit()
        flash("Successfully created assessment.")
        return redirect(url_for('index'))

    return render_template('AddAssessment.html', assessment_form=assessment_form)

@app.route('/manage-assessments')
@login_required
def manageAssessments():
    assessments = Assessment.query.all()
    return render_template('ManageAssessments.html', assessments=assessments)