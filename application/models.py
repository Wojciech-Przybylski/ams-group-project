import re
from application import db
from wtforms.validators import ValidationError
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password = db.Column(db.String(512), nullable=False)
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

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
    # def set_quantity(self, product_id, quantity):
    #     cart_item = CartItem.query.filter_by(product_id=product_id, cart_id=self.id).first()
    #     if cart_item:
    #         if quantity > 0:
    #             cart_item.quantity = quantity
    #             db.session.commit()
    #         else:
    #             db.session.delete(cart_item)
    #             db.session.commit()
    
    # def add_item(self, product_id):
    #     cart_item = CartItem.query.filter_by(product_id=product_id, cart_id=self.id).first()
    #     if cart_item:
    #         cart_item.quantity += 1
    #         db.session.commit()
    #     else:
    #         new_cart_item = CartItem(product_id=product_id, quantity=1, cart_id=self.id)
    #         db.session.add(new_cart_item)
    #         db.session.commit()
    
    # def remove_item(self, product_id):
    #     cart_item = CartItem.query.filter_by(product_id=product_id, cart_id=self.id).first()
    #     if cart_item:
    #         db.session.delete(cart_item)
    #         db.session.commit()

    # def empty_cart(self):
    #     cart_items = CartItem.query.filter_by(cart_id=self.id).all()
    #     for item in cart_items:
    #         db.session.delete(item)
    #         db.session.commit()
        
    
# class CartItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)

    
# class CartDisplay():
#     def __init__(self, product_id, name, price, quantity, image) -> None:
#         self.id = product_id
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.image = image

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
        
