from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from application.models import CheckAdmin, BannedChars, User, Category, Product, CheckPostcode

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30), BannedChars()])
    email = StringField('Email', validators=[DataRequired(), Email(), BannedChars()])
    password = PasswordField('Password', validators=[DataRequired(), BannedChars()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), BannedChars()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        admin = CheckAdmin(username.data)
        if user:
            raise ValidationError('That username is taken. Please choose another one.')
        elif admin:
            raise ValidationError('That username is not allowed. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        admin = CheckAdmin(email.data)
        if user:
            raise ValidationError('That email is taken. Please choose another one.')
        elif admin:
            raise ValidationError('That email is not allowed. Please choose another one.')