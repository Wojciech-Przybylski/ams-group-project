import pytest
from application import app, db, bcrypt
from application.models import Genres, User, PaymentDetails, CommentThread, Comments, Movies, MovieGenres, Actors, MovieActors, Directors, MovieDirectors, Showings, Bookings, BookingsItems, TicketType, Cart, CartItem, CommentView, BannedChars, CheckAdmin
from datetime import datetime
from wtforms.validators import ValidationError
from wtforms import Form, StringField

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

def test_User(client):
    
    # Create a user
    user = User(name="bob", email="bob@qa.com", password=bcrypt.generate_password_hash("234"))
    # Add the user to the database
    db.session.add(user)
    db.session.commit()
    # Retrieve the user from the database
    retrieved_user = User.query.filter_by(id=3).first()
    # Assert that the retrieved user's name matches the expected value
    assert retrieved_user.name == 'bob'
    assert retrieved_user.email == 'bob@qa.com'
    assert bcrypt.check_password_hash(retrieved_user.password, "234")

def test_PaymentDetails(client):
    # Create a user (for the ForeignKey relationship)
    user = User(name="Alice", email="alice@example.com", password="hashed_password")
    db.session.add(user)
    db.session.commit()

    # Create a payment detail
    payment_detail = PaymentDetails(
        card_name="Alice Smith",
        user_id=user.id,
        card_number="1234567890123456",
        expiry_date="12/25",
        security_code="123"
    )

    # Add the payment detail to the database
    db.session.add(payment_detail)
    db.session.commit()

    # Retrieve the payment detail from the database
    retrieved_payment_detail = PaymentDetails.query.filter_by(id=1).first()

    # Assert that the retrieved payment detail matches the expected values
    assert retrieved_payment_detail.card_name == "Alice Smith"
    assert retrieved_payment_detail.user_id == user.id
    assert retrieved_payment_detail.card_number == "1234567890123456"
    assert retrieved_payment_detail.expiry_date == "12/25"
    assert retrieved_payment_detail.security_code == "123"
    
def test_Comments(client):
    # Create a comment thread
    comment_thread = CommentThread(title="Movie Discussion Thread")
    db.session.add(comment_thread)
    db.session.commit()

    # Create a user
    user = User(name="Alice", email="alice@example.com", password="hashed_password")
    db.session.add(user)
    db.session.commit()

    # Create a comment
    comment = Comments(comment_thread_id=comment_thread.id, user_id=user.id, comment="This is a comment")

    # Add the comment to the database
    db.session.add(comment)
    db.session.commit()

    # Retrieve the comment from the database
    retrieved_comment = Comments.query.filter_by(id=1).first()

    # Assert that the retrieved comment matches the expected values
    assert retrieved_comment.comment == "This is a comment"
    
def test_Movies(client):
    # Create a movie
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"  # Replace with the desired release date
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()

    # Retrieve the movie from the database
    retrieved_movie = Movies.query.filter_by(id=1).first()

    # Assert that the retrieved movie matches the expected values
    assert retrieved_movie.title == "Test Movie"
    assert retrieved_movie.description == "This is a test movie description."
    assert retrieved_movie.image == "test_movie.jpg"
    assert retrieved_movie.release_date.strftime('%Y-%m-%d') == "2023-09-10"
    
def test_Genres_and_MovieGenres(client):
    # Create a movie genre
    genre = Genres(genre="Action")

    # Add the genre to the database
    db.session.add(genre)
    db.session.commit()

    # Create a movie
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()

    # Create a MovieGenres association between the movie and genre
    movie_genre = MovieGenres(movie_id=movie.id, genre_id=genre.id)

    # Add the association to the database
    db.session.add(movie_genre)
    db.session.commit()

    # Retrieve the movie genre association from the database
    retrieved_movie_genre = MovieGenres.query.filter_by(id=1).first()

    # Assert that the retrieved association matches the expected values
    assert retrieved_movie_genre.movie_id == movie.id
    assert retrieved_movie_genre.genre_id == genre.id

def test_Actors_and_MovieActors(client):
    # Create an actor
    actor = Actors(actor="John Doe")

    # Add the actor to the database
    db.session.add(actor)
    db.session.commit()

    # Create a movie
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()

    # Create a MovieActors association between the movie and actor
    movie_actor = MovieActors(movie_id=movie.id, actor_id=actor.id)

    # Add the association to the database
    db.session.add(movie_actor)
    db.session.commit()

    # Retrieve the movie actor association from the database
    retrieved_movie_actor = MovieActors.query.filter_by(id=1).first()

    # Assert that the retrieved association matches the expected values
    assert retrieved_movie_actor.movie_id == movie.id
    assert retrieved_movie_actor.actor_id == actor.id
    
def test_Directors_and_MovieDirectors(client):
    # Create a director
    director = Directors(director="Jane Smith")

    # Add the director to the database
    db.session.add(director)
    db.session.commit()

    # Create a movie
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()

    # Create a MovieDirectors association between the movie and director
    movie_director = MovieDirectors(movie_id=movie.id, director_id=director.id)

    # Add the association to the database
    db.session.add(movie_director)
    db.session.commit()

    # Retrieve the movie director association from the database
    retrieved_movie_director = MovieDirectors.query.filter_by(id=1).first()

    # Assert that the retrieved association matches the expected values
    assert retrieved_movie_director.movie_id == movie.id
    assert retrieved_movie_director.director_id == director.id
    
def test_Showings(client):
    # Create a movie
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()

    # Create a showing
    showing = Showings(
        movie_id=movie.id,
        screen_number=1,
        date=datetime.utcnow(),
        seats_available=100
    )

    # Add the showing to the database
    db.session.add(showing)
    db.session.commit()

    # Retrieve the showing from the database
    retrieved_showing = Showings.query.filter_by(id=1).first()

    # Assert that the retrieved showing matches the expected values
    assert retrieved_showing.movie_id == movie.id
    assert retrieved_showing.screen_number == 1
    assert isinstance(retrieved_showing.date, datetime)
    assert retrieved_showing.seats_available == 100
    
def test_Bookings_and_BookingsItems(client):
    # Create a user
    user = User(name="Alice", email="alice@example.com", password="hashed_password")

    # Add the user to the database
    db.session.add(user)
    db.session.commit()

    # Create a movie
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()

    # Create a showing
    showing = Showings(
        movie_id=movie.id,
        screen_number=1,
        date=datetime.utcnow(),
        seats_available=100
    )

    # Add the showing to the database
    db.session.add(showing)
    db.session.commit()

    # Create a ticket type
    ticket_type = TicketType(ticket_type="Standard", price=10)

    # Add the ticket type to the database
    db.session.add(ticket_type)
    db.session.commit()

    # Create a booking
    booking = Bookings(
        user_id=user.id,
        movie_id=movie.id,
        date=datetime.utcnow()
    )

    # Add the booking to the database
    db.session.add(booking)
    db.session.commit()

    # Create a booking item
    booking_item = BookingsItems(
        booking_id=booking.id,
        showing_id=showing.id,
        ticket_type_id=ticket_type.id,
        quantity=2
    )

    # Add the booking item to the database
    db.session.add(booking_item)
    db.session.commit()

    # Retrieve the booking and booking item from the database
    retrieved_booking = Bookings.query.filter_by(id=1).first()
    retrieved_booking_item = BookingsItems.query.filter_by(id=1).first()

    # Assert that the retrieved booking and booking item match the expected values
    assert retrieved_booking.user_id == user.id
    assert retrieved_booking.movie_id == movie.id
    assert isinstance(retrieved_booking.date, datetime)

    assert retrieved_booking_item.booking_id == booking.id
    assert retrieved_booking_item.showing_id == showing.id
    assert retrieved_booking_item.ticket_type_id == ticket_type.id
    assert retrieved_booking_item.quantity == 2

def test_Cart_empty_cart(client):
    # Create a user
    user = User(name="Alice", email="alice@example.com", password="hashed_password")
    db.session.add(user)
    db.session.commit()

    # Create a cart for the user
    cart = Cart(user_id=user.id)
    db.session.add(cart)
    db.session.commit()

    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    db.session.add(movie)
    db.session.commit()

    # Create a showing
    showing = Showings(
        movie_id=1,  # Replace with actual movie_id
        screen_number=1,
        date=datetime.utcnow(),
        seats_available=100
    )
    db.session.add(showing)
    db.session.commit()

    # Create a ticket type
    ticket_type = TicketType(
        ticket_type="Standard",
        price=10
    )
    db.session.add(ticket_type)
    db.session.commit()

    # Create some cart items for the cart
    cart_item1 = CartItem(showing_id=showing.id, ticket_type_id=ticket_type.id, quantity=2, cart_id=cart.id)
    cart_item2 = CartItem(showing_id=showing.id, ticket_type_id=ticket_type.id, quantity=3, cart_id=cart.id)
    db.session.add(cart_item1)
    db.session.add(cart_item2)
    db.session.commit()

    # Check that cart items exist before emptying
    assert CartItem.query.filter_by(cart_id=cart.id).count() == 2

    # Call the empty_cart method
    cart.empty_cart()

    # Check that cart items are deleted after emptying
    assert CartItem.query.filter_by(cart_id=cart.id).count() == 0

def test_comment_view():
    comment = CommentView(id=1, user_name='John', comment='Hello', time='2023-09-08 14:30:00')
    assert comment.id == 1
    assert comment.user_name == 'John'
    assert comment.comment == 'Hello'
    assert comment.time == '2023-09-08 14:30:00'

def test_banned_chars_validator_valid_input():
    form = Form()
    field = StringField(validators=[BannedChars()])
    field.data = 'Hello123'
    assert BannedChars()(form, field) is None  # Should not raise ValidationError

def test_banned_chars_validator_invalid_input():
    form = Form()
    field = StringField(validators=[BannedChars()])
    field.data = 'Hello$'
    with pytest.raises(ValidationError):
        BannedChars()(form, field)  # Should raise ValidationError

def test_check_admin_validator_valid_input():
    form = Form()
    field = StringField(validators=[CheckAdmin()])
    field.data = 'John'
    assert CheckAdmin()(form, field) is None  # Should not raise ValidationError

def test_check_admin_validator_invalid_input():
    form = Form()
    field = StringField(validators=[CheckAdmin()])
    field.data = 'admin'
    with pytest.raises(ValidationError):
        CheckAdmin()(form, field)  # Should raise ValidationError
