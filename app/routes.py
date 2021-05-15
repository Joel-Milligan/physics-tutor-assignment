from datetime import datetime
from flask import render_template, flash, redirect, request
from flask.helpers import url_for
from flask_login import current_user, login_user, login_required
from sqlalchemy.sql.functions import now
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User

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


@app.route('/register', methods=['POST'])
def register():
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
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/content')
@login_required
def content():
    return render_template('TeachingPage.html')