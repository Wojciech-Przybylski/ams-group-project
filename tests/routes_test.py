import app
from flask import session, render_template
from application.models import User, Movies, Cart, CartItem, Showings, Bookings, BookingsItems, Genres, Actors, Directors, MovieGenres, MovieActors, MovieDirectors, CommentThread, Comments, CommentView, TicketType
from application import app, db, bcrypt
from application.forms import CreateCommentForm
from flask_testing import TestCase
from datetime import datetime, timedelta
import pytest
from flask import url_for
import pytest
from application import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()
        db.create_all()


def test_home_route(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Home' in response.data
    assert b'<!DOCTYPE html>' in response.data  # Add more specific content checks as needed
    
    
def test_signup_route(client):
    # Simulate a GET request to the /signup route
    response = client.get('/signup')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected title
    assert b'<title>Sign Up</title>' in response.data

    # Simulate a POST request to the /signup route with valid form data
    user_data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'testpassword'
    }
    response = client.post('/signup', data=user_data, follow_redirects=True)

    # Check if the response status code is 200 (OK) after successful signup
    assert response.status_code == 200

    # Check if the response contains the expected redirect to the home page
    assert b'Home' in response.data
    
    user = User(name="Test User'", email="test@example.com", password=bcrypt.generate_password_hash("testpassword"))
    # Add the user to the database
    db.session.add(user)
    db.session.commit()

    # Check if a new user has been added to the database
    new_user = User.query.filter_by(email='test@example.com').first()
    assert new_user is not None

    # Clean up: Delete the newly created user from the database (if needed)
    if new_user:
        db.session.delete(new_user)
        db.session.commit()
    if new_user:
        db.session.delete(user)
        db.session.commit()

def test_login_route(client):
    # Create a sample user for testing
    sample_user = User(
        name='Test User',
        email='test@example.com',
        password='testpassword'  # Ensure this matches the hashed password stored in your database
    )
    db.session.add(sample_user)
    db.session.commit()

    # Simulate a GET request to the /login route
    response = client.get('/login')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected title
    assert b'<title>Login</title>' in response.data

    # Simulate a POST request to the /login route with valid form data
    login_data = {
        'email': 'test@example.com',
        'password': 'testpassword'
    }
    response = client.post('/login', data=login_data, follow_redirects=True)

    # Check if the response status code is 200 (OK) after successful login
    assert response.status_code == 200

    # Check if the response contains the expected redirect to the home page
    assert b'Home' in response.data


    # Clean up: Delete the sample user from the database (if needed)
    db.session.delete(sample_user)
    db.session.commit()


def test_signup_form_validation(client):
    # Simulate a POST request with invalid form data
    response = client.post('/signup', data={}, follow_redirects=True)

    # Check if the form validation errors are displayed
    assert response.status_code == 200  # You may need to adjust the status code based on your actual implementation

def test_movies_route(client):
    # Insert a sample movie into the database for testing
    sample_movie = Movies(
        title='Sample Movie',
        description='Sample Description',
        image='sample_image.jpg',  # Placeholder image value
        release_date=datetime(2023, 9, 15)  # Provide a placeholder release date
    )
    db.session.add(sample_movie)
    db.session.commit()

    # Simulate a GET request to the /movies route
    response = client.get('/movies')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the movie title is present in the response
    assert b'Sample Movie' in response.data

    # Clean up: Delete the sample movie from the database
    db.session.delete(sample_movie)
    db.session.commit()

def test_movie_route(client):
    # Insert a sample movie and related data into the database for testing
    sample_movie = Movies(
        title='Sample Movie',
        description='Sample Description',
        image='sample_image.jpg',
        release_date=datetime(2023, 9, 15)
    )
    sample_genre = Genres(genre='Action')
    sample_actor = Actors(actor='John Doe')
    sample_director = Directors(director='Jane Smith')

    db.session.add_all([sample_movie, sample_genre, sample_actor, sample_director])
    db.session.commit()

    movie_genre = MovieGenres(movie_id=sample_movie.id, genre_id=sample_genre.id)
    movie_actor = MovieActors(movie_id=sample_movie.id, actor_id=sample_actor.id)
    movie_director = MovieDirectors(movie_id=sample_movie.id, director_id=sample_director.id)

    db.session.add_all([movie_genre, movie_actor, movie_director])
    db.session.commit()

    # Simulate a GET request to the /movie/<movie_id> route (replace <movie_id> with the actual movie ID)
    movie_id = sample_movie.id
    response = client.get(f'/movie/{movie_id}')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if movie title is present in the response
    assert b'Sample Movie' in response.data

    # Check if genre, actor, and director names are present in the response
    assert b'Action' in response.data
    assert b'John Doe' in response.data
    assert b'Jane Smith' in response.data
    
def test_new_releases_route(client):
    # Insert some sample movies into the database with recent release dates (within 3 months)
    # Replace the placeholders with actual data as needed
    sample_movies = [
        Movies(
            title='New Release 1',
            description='Description 1',
            image='image1.jpg',
            release_date=datetime(2023, 8, 1)  # Within 3 months
        ),
        Movies(
            title='New Release 2',
            description='Description 2',
            image='image2.jpg',
            release_date=datetime(2023, 8, 15)  # Within 3 months
        ),
        Movies(
            title='Old Movie',
            description='Description 3',
            image='image3.jpg',
            release_date=datetime(2023, 6, 1)  # Older than 3 months
        ),
    ]

    db.session.add_all(sample_movies)
    db.session.commit()

    # Simulate a GET request to the /new-releases route
    response = client.get('/new-releases')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the titles of the new releases are present in the response
    assert b'New Release 1' in response.data
    assert b'New Release 2' in response.data

    # Check if the title of the old movie is NOT present in the response
    assert b'Old Movie' not in response.data

    # Clean up: Delete the sample movies from the database
    for movie in sample_movies:
        db.session.delete(movie)
    db.session.commit()
    
def test_logout_route(client):
    # Simulate a GET request to the /logout route
    response = client.get('/logout', follow_redirects=True)

    # Check if the response status code is 200 (OK) after successful logout
    assert response.status_code == 200

    # Check if the response contains the expected redirect to the home page
    assert b'Home' in response.data

    # Check if the 'user_id' and 'admin' session variables are cleared
    with client.session_transaction() as session:
        assert 'user_id' not in session
        assert 'admin' not in session
    
def test_discussion_board_route(client):
    # Simulate a GET request to the /discussion-board route
    response = client.get('/discussion-board')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 302
    assert b'/login' in response.headers['Location'].encode('utf-8')  

    # Simulate a POST request to the /discussion-board route (assuming the user is logged in)
    with client.session_transaction() as session:
        session['id'] = 1  # Replace with a valid user ID if needed

    response = client.post('/discussion-board', data={'title': 'New Thread Title'})

    # Check if the response status code is 302 (redirect) after posting a new thread
    assert response.status_code == 302

    # Check if the new thread is added to the database
    new_thread = CommentThread.query.filter_by(title='New Thread Title').first()
    assert new_thread is not None

    # Clean up: Delete the newly created thread from the database (assuming you have a way to delete threads)
    if new_thread:
        db.session.delete(new_thread)
        db.session.commit()

def test_thread_route_authenticated(client):
    
    # Create a sample user for testing
    sample_user = User(
        name='Test User',
        email='test@example.com',
        password='testpassword'  # Ensure this matches the hashed password stored in your database
    )
    db.session.add(sample_user)
    db.session.commit()

    # Create a sample comment thread for testing
    sample_thread = CommentThread(
        title='Sample Thread Title'
    )
    db.session.add(sample_thread)
    db.session.commit()

    # Simulate a user login by setting 'user_id' in the session
    with client.session_transaction() as session:
        session['user_id'] = sample_user.id

    # Simulate a GET request to the /discussion-board/<thread_id> route
    thread_id = sample_thread.id  # Use the ID of the sample thread created above
    response = client.get(f'/discussion-board/{thread_id}')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected thread title
    assert b'Sample Thread Title' in response.data

    # Simulate a POST request with valid form data to add a comment
    comment_data = {
        'comment': 'Test Comment'
    }
    response = client.post(f'/discussion-board/{thread_id}', data=comment_data, follow_redirects=True)

    # Check if the response status code is 200 (OK) after posting a comment
    assert response.status_code == 200

    # Check if the response contains the expected redirect back to the thread page
    assert b'Sample Thread Title' in response.data

    # Check if the new comment is added to the database
    new_comment = Comments.query.filter_by(comment_thread_id=thread_id).first()
    assert new_comment is not None
    assert new_comment.comment == 'Test Comment'
    

def test_delete_comment_route(client):
    # Create a sample user for testing
    sample_user = User(
        name='Test User',
        email='test@example.com',
        password='testpassword'  # Ensure this matches the hashed password stored in your database
    )
    db.session.add(sample_user)
    db.session.commit()

    # Create a sample comment thread for testing
    sample_thread = CommentThread(
        title='Sample Thread Title'
    )
    db.session.add(sample_thread)
    db.session.commit()

    # Create a sample comment associated with the sample thread
    sample_comment = Comments(
        comment_thread_id=sample_thread.id,  # Use the ID of the sample thread
        user_id=sample_user.id,
        comment='Sample Comment'
    )
    db.session.add(sample_comment)
    db.session.commit()

    # Get the comment ID for the sample comment
    comment_id = sample_comment.id

    # Simulate a GET request to the /delete-comment/<comment_id> route
    response = client.get(f'/delete-comment/{comment_id}')

    # Check if the response status code is 302 (redirect)
    assert response.status_code == 302

    # Check if the comment is deleted from the database
    deleted_comment = Comments.query.get(comment_id)
    assert deleted_comment is None

    # Clean up: Delete the sample user, thread, and any other related records
    db.session.delete(sample_user)
    db.session.delete(sample_thread)
    db.session.commit()


def test_opening_times_route(client):
    # Simulate a GET request to the /opening-times route
    response = client.get('/opening-times')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected title
    assert b'<title>Opening Times</title>' in response.data
    
def test_book_tickets_route(client):
    # Create a sample user for testing
    sample_user = User(
        name='Test User',
        email='test@example.com',
        password='testpassword'  # Ensure this matches the hashed password stored in your database
    )
    db.session.add(sample_user)
    db.session.commit()

    # Create a sample movie for testing
    sample_movie = Movies(
        title='Sample Movie',
        description='Sample Description',
        image='sample_image.jpg',
        release_date=datetime(2023, 9, 15)
    )
    db.session.add(sample_movie)
    db.session.commit()

    # Create a sample showing for the sample movie with a valid screen number
    sample_showing = Showings(
        movie_id=sample_movie.id,
        screen_number=1,  # Set a valid screen number
        date=datetime(2023, 9, 20, 18, 0, 0),  # Set the date and time for the showing
        seats_available=50  # Set the number of available seats
    )
    db.session.add(sample_showing)
    db.session.commit()

    # Log in the sample user by setting the 'user_id' in the session
    with client.session_transaction() as session:
        session['user_id'] = sample_user.id

    # Simulate a GET request to the /book/<movie_id> route
    movie_id = sample_movie.id
    response = client.get(f'/book/{movie_id}')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the sample movie title is present in the response
    assert b'Sample Movie' in response.data

def test_payment_route(client):
    # Create a sample user for testing
    sample_user = User(
        name='Test User',
        email='test@example.com',
        password='testpassword'  # Ensure this matches the hashed password stored in your database
    )
    db.session.add(sample_user)
    db.session.commit()

    # Log in the sample user by setting the 'user_id' in the session
    with client.session_transaction() as session:
        session['user_id'] = sample_user.id

    # Create a sample cart and cart items for the user
    sample_cart = Cart(user_id=sample_user.id)
    db.session.add(sample_cart)
    db.session.commit()

    # Create a sample showing and related movie for testing
    sample_movie = Movies(
        title='Sample Movie',
        description='Sample Description',
        image='sample_image.jpg',
        release_date=datetime(2023, 9, 15)
    )
    db.session.add(sample_movie)
    db.session.commit()

    sample_showing = Showings(
        movie_id=sample_movie.id,
        screen_number=1,  # Set a valid screen number
        date=datetime(2023, 9, 20, 18, 0, 0),  # Set the date and time for the showing
        seats_available=50  # Set the number of available seats
    )
    db.session.add(sample_showing)
    db.session.commit()

    # Simulate a GET request to the /payment route
    response = client.get('/payment')

    # Check if the response status code is 200 (OK) since the user is logged in
    assert response.status_code == 200


def test_confirmation_route(client):
    # Create a sample user for testing
    sample_user = User(
        name='Test User',
        email='test@example.com',
        password='testpassword'  # Ensure this matches the hashed password stored in your database
    )
    db.session.add(sample_user)
    db.session.commit()

    # Log in the sample user by setting the 'user_id' in the session
    with client.session_transaction() as session:
        session['user_id'] = sample_user.id

    # Create a sample booking and related booking items for testing
    sample_movie = Movies(
        title='Sample Movie',
        description='Sample Description',
        image='sample_image.jpg',
        release_date=datetime(2023, 9, 15)
    )
    db.session.add(sample_movie)
    db.session.commit()
    
    sample_showing = Showings(
        movie_id=sample_movie.id,
        screen_number=1,  # Set a valid screen number
        date=datetime(2023, 9, 20, 18, 0, 0),  # Set the date and time for the showing
        seats_available=50  # Set the number of available seats
    )
    db.session.add(sample_showing)
    db.session.commit()

    sample_booking = Bookings(
        user_id=sample_user.id,
        movie_id=sample_movie.id,
        date=datetime.utcnow()
    )
    db.session.add(sample_booking)
    db.session.commit()
    
    sample_ticket_type = TicketType(
        ticket_type= 'regular',
        price= 1.50        
    )
    db.session.add(sample_ticket_type)
    db.session.commit()

    sample_booking_item = BookingsItems(
        booking_id=sample_booking.id,
        showing_id=sample_showing.id,  # Replace with a valid showing ID
        ticket_type_id=sample_ticket_type.id,  # Replace with a valid ticket type ID
        quantity=2  # Set the quantity of tickets
    )
    db.session.add(sample_booking_item)
    db.session.commit()

    # Simulate a GET request to the /confirmation route with the sample booking ID
    response = client.get(f'/confirmation/{sample_booking.id}')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200



def test_get_remaining_tickets_route(client):
    # Create a sample showing record in the database with seats_available
    showing_id = 1  # Replace with a valid showing ID from your database
    seats_available = 10  # Set the seats available for testing

    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )

    # Add the movie to the database
    db.session.add(movie)
    db.session.commit()
    # Insert the sample showing record into the database
    showing = Showings(id=showing_id, seats_available=seats_available, movie_id=1, screen_number=1)
    db.session.add(showing)
    db.session.commit()

    # Simulate a GET request to the /get_remaining_tickets/<showing_id> route
    response = client.get(f'/get_remaining_tickets/{showing_id}')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected remaining tickets count as a string
    expected_tickets_count = str(seats_available)
    assert response.data.decode('utf-8') == expected_tickets_count

    # Clean up: Delete the sample showing record from the database
    db.session.delete(showing)
    db.session.commit()
    
def test_search_redirects_to_results(client):
    movie = Movies(
        title="Test Movie",
        description="This is a test movie description.",
        image="test_movie.jpg",
        release_date="2023-09-10"
    )
    db.session.add(movie)
    db.session.commit()

    # Simulate a POST request to the /search route with a search query
    response = client.post('/search', data={'search': 'Test Movie'})

    # Check if the response status code is 302 (redirect)
    assert response.status_code == 302

def test_search_results_route(client):
    
    movie = Movies(
    title="Test Movie",
    description="This is a test movie description.",
    image="test_movie.jpg",
    release_date="2023-09-10"
)
    db.session.add(movie)
    db.session.commit()
    
    # Simulate a GET request to the /search_results route with a search query
    response = client.get('/search_results?search=Test+Movie')

    # Check if the response status code is 200 (OK) or any other appropriate status code
    assert response.status_code == 200

    # Check if the response contains the expected search results for 'Test Movie'
    assert b'Test Movie' in response.data
    
def test_search_results_route(client):
    # Simulate a GET request to the /search-results route with a search query
    
    movie = Movies(
    title="Test Movie",
    description="This is a test movie description.",
    image="test_movie.jpg",
    release_date="2023-09-10"
)
    db.session.add(movie)
    db.session.commit()
    
    response = client.get('/search-results/movie')

    # Check if the response status code is 200 (OK) or any other appropriate status code
    assert response.status_code == 200

    # Check if the response contains the expected search results for 'Movie'
    assert b'Test Movie' in response.data

    actor = Actors(actor="John Doe")

    # Add the actor to the database
    db.session.add(actor)
    db.session.commit()
    
    director = Directors(director="Jane Smith")

    # Add the director to the database
    db.session.add(director)
    db.session.commit()
    
    genre = Genres(genre="Action")

    # Add the genre to the database
    db.session.add(genre)
    db.session.commit()

    # Check if the response does not contain results for other search terms
    assert b'Actor Name' not in response.data
    assert b'Director Name' not in response.data
    assert b'Genre Name' not in response.data
    
def test_classifications_route(client):
    # Simulate a GET request to the /classifications route
    response = client.get('/classifications')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # You can add more specific checks for the content of the 'classifications' template if needed

def test_about_route(client):
    # Simulate a GET request to the /about route
    response = client.get('/about')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # You can add more specific checks for the content of the 'about' template if needed

def test_contact_route(client):
    # Simulate a GET request to the /contact-us route
    response = client.get('/contact-us')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # You can add more specific checks for the content of the 'contact' template if needed

def test_screens_route(client):
    # Simulate a GET request to the /screens route
    response = client.get('/screens')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200