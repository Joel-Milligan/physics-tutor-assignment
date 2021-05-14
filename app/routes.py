from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Setup login form
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print("logining in")
        print('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect('/')

    # Setup registration form
    register_form = RegisterForm()

    return render_template('LoginRegisterPage.html', login_form=login_form, register_form=register_form)


@app.route('/register', methods=['POST'])
def register():
 
    # Setup registration form
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        print("registering")
        print('Register requested for user {}'.format(
            register_form.username.data))
        return redirect('/')