import re
from application import db
from wtforms.validators import ValidationError
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True, index=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    bookings = db.relationship('Bookings', backref='user', lazy=True)

class PaymentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    card_number = db.Column(db.String(16), nullable=False, unique=True, index=True)
    expiry_date = db.Column(db.String(5), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)

class CommentThread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True, index=True)
    comments = db.relationship('Comments', backref='comment_thread', lazy=True)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_thread_id = db.Column(db.Integer, db.ForeignKey('comment_thread.id'), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    comment = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True, index=True)
    description = db.Column(db.String(2048), nullable=False)
    image = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(30), nullable=False, unique=True, index=True)

class MovieGenres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False, index=True)

class Actors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.String(30), nullable=False, unique=True, index=True)

class MovieActors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False, index=True)

class Directors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director = db.Column(db.String(30), nullable=False, unique=True, index=True)

class MovieDirectors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False, index=True)


class Showings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    screen_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seats_available = db.Column(db.Integer, nullable=False)

class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class BookingsItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False, index=True)
    showing_id = db.Column(db.Integer, db.ForeignKey('showings.id'), nullable=False, index=True)
    ticket_type_id = db.Column(db.Integer, db.ForeignKey('ticket_type.id'), nullable=False, index=True)
    quantity = db.Column(db.Integer, nullable=False)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def empty_cart(self):
        cart_items = CartItem.query.filter_by(cart_id=self.id).all()
        for item in cart_items:
            db.session.delete(item)
            db.session.commit()
        
    
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    showing_id = db.Column(db.Integer, db.ForeignKey('showings.id'), nullable=False)
    ticket_type_id = db.Column(db.Integer, db.ForeignKey('ticket_type.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)

class TicketType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.String(30), nullable=False, unique=True, index=True)
    price = db.Column(db.Integer, nullable=False)

class CommentView:
    def __init__(self, id, user_name, comment, time) -> None:
        self.id = id
        self.user_name = user_name
        self.comment= comment
        self.time = time

class BannedChars(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        regex = re.compile('[^a-zA-Z0-9]')
        if regex.search(field.data):
            raise ValidationError('Please only use alphanumeric characters.')
        
class CheckAdmin(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() == 'admin':
            raise ValidationError('Name cannot be "admin".')
        
class ValidateTicketNumber(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        child_ticket_number = form.child_tickets.data
        adult_ticket_number = form.adult_tickets.data
        # get total tickets available from db
        showing = Showings.query.filter_by(id=form.showing_id.data).first()
        total_tickets_available = showing.seats_available
        total_tickets_requested = child_ticket_number + adult_ticket_number
        print(f'Total tickets requested: {child_ticket_number + adult_ticket_number}')
        print(f'total tickets available: {total_tickets_available}')
        # check if total tickets requested is greater than total tickets available
        if total_tickets_requested > total_tickets_available:
            print('Total tickets requested is greater than total tickets available.')
            raise ValidationError('Total tickets requested is greater than total tickets available.')
        
class SpecialCharacterPassword(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        regex = re.compile(r'^(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-])(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$')
        if not regex.search(field.data):
            raise ValidationError('Password must contain at least one uppercase chacter, one lowercase character, one number, and one special character.')
        
        
