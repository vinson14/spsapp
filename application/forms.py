from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignupForm(FlaskForm):
    """Signup Form"""
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=6, message='Username must be at least 6 characters.')])
    name = StringField('Name', validators=[DataRequired()])
    password =  PasswordField('Password', validators=[DataRequired(),
                            Length(min=8, message='Username must be at least 8 characters.')])
    email = StringField('Email', validators=[DataRequired(),
                        Email(message='Please enter a valid email')])
    confirm_pass = PasswordField('Please re-enter your password', validators=[DataRequired(),
                            EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')
