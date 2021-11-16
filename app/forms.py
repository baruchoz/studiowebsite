from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, IntegerField, 
                    BooleanField, DateTimeField, RadioField, SelectField, 
                    TextField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo, Regexp
from flask_wtf.recaptcha import validators




class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')