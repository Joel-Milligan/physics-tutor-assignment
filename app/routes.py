from flask import render_template
from app import app
from app.forms import LoginForm, RegisterForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('LoginRegisterPage.html', login_form=LoginForm(), register_form=RegisterForm())