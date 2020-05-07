from flask import Blueprint, redirect, render_template, flash, request
from flask import session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from datetime import datetime as dt
from .forms import SignupForm, LoginForm
from .models import db, User
from . import login_manager, socketio, emit

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Creates a page for users to signup"""
    form = SignupForm()
    if form.validate_on_submit():
        check_username = User.query.filter_by(username=form.username.data).first()
        check_email = User.query.filter_by(email=form.email.data).first()
        if check_username == None and check_email == None:
            user = User(username=form.username.data, name=form.name.data,
                        email=form.email.data, created=dt.now())
            user.set_password(form.password.data)
            user.add_user()
            login_user(user) # Set user as logged in
            return redirect(url_for('main_bp.dashboard'))
    return render_template("signup.html", form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    form = LoginForm()
    username = form.username.data
    if form.validate_on_submit():
        user = User.query.filter((User.username == username) | (User.email == username)).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main_bp.dashboard'))
    return render_template("login.html", form=form)


@socketio.on('check username')
def check_username(data):
    """Check in realtime if the username is taken"""
    username = data['username']
    check_username = User.query.filter_by(username=username).first()
    valid_username = check_username == None
    emit("valid username", valid_username, broadcast=True)


@socketio.on('check email')
def check_email(data):
    """Check in realtime if the email is taken"""
    email = data['email']
    check_email = User.query.filter_by(email=email).first()
    valid_email = check_email == None
    emit("valid email", valid_email, broadcast=True)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
