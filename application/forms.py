from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from application.models import CheckAdmin, BannedChars, User, ValidateTicketNumber, Showings, SpecialCharacterPassword
from wtforms import Form, IntegerField, SelectField, SubmitField, validators


class SignUpForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=30), BannedChars(), CheckAdmin(message="Name cannot be 'admin'.")])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=30), SpecialCharacterPassword()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=2, max=30), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists.')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Login')

class CreateThreadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Create Thread')

class CreateCommentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Create Comment')

class BookingForm(FlaskForm):
    showing_id = SelectField('Showing Times', coerce=int)
    child_tickets = IntegerField('Child Tickets', validators=[ValidateTicketNumber()])
    adult_tickets = IntegerField('Adult Tickets', validators=[ValidateTicketNumber()])
    submit = SubmitField('Next: Payment')


class PaymentForm(FlaskForm):
    card_name = StringField('Cardholder Name', validators=[DataRequired(), Length(min=2, max=30), BannedChars()])
    card_number = StringField('Card Number', validators=[DataRequired(), Length(min=16, max=16), BannedChars(), Regexp('^[0-9]*$', message='Card number must be numeric.')])
    expiry_date = StringField('Expiry Date', validators=[DataRequired(), Length(min=5, max=7), BannedChars(), Regexp('^(0[1-9]|1[0-2])\/(0[0-9]|1[0-9]|2[0-9]|3[0-9])$', message='Expiry date must be in format MM/YY.')])
    security_code = StringField('Security Code', validators=[DataRequired(), Length(min=3, max=4), BannedChars(), Regexp('^[0-9]*$', message='Security code must be numeric.')])
    submit = SubmitField('Pay')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired(), Length(min=1, max=128)])
    submit = SubmitField('Search')