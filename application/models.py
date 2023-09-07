import re
from application import db
from wtforms.validators import ValidationError
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True, index=True)
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
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
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
    genre = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False, index=True)

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
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seats = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False, index=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seat = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    showing = db.Column(db.Integer, db.ForeignKey('showings.id'), nullable=False, index=True)

