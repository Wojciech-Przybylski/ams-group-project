import pytest
from application import app, db, bcrypt
from application.models import Genres, User, PaymentDetails, CommentThread, Comments, Movies

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

def test_Genres(client):
    # Create a movie genre
    genre = Genres(genre="Noir")
    # Add the genre to the database
    db.session.add(genre)
    db.session.commit()
    # Retrieve the movie genre from the database
    retrieved_genre = Genres.query.filter_by(genre=genre.genre).first()
    # Assert that the retrieved genre matches the expected value
    assert retrieved_genre.genre == 'Noir'

def test_User(client):
    
    # Create a user
    user = User(name="Bob", email="bob@qa.com", password=bcrypt.generate_password_hash("123"))
    # Add the user to the database
    db.session.add(user)
    db.session.commit()
    # Retrieve the user from the database
    retrieved_user = User.query.filter_by(id=1).first()
    # Assert that the retrieved user's name matches the expected value
    assert retrieved_user.name == 'Bob'
    assert retrieved_user.email == 'bob@qa.com'
    assert bcrypt.check_password_hash(retrieved_user.password, "123")

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