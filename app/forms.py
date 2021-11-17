from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, IntegerField, BooleanField)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.recaptcha import validators
from wtforms.widgets.core import TextArea



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired(), Email()])
    submit = SubmitField()