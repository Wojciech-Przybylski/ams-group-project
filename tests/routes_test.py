import app
from flask import session
from application.models import User, Movies, Cart, CartItem, Showings, Bookings, BookingsItems, Genres, Actors, Directors, MovieGenres, MovieActors, MovieDirectors, CommentThread, Comments, CommentView
from application import app, db, bcrypt
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

def test_home_route(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Home' in response.data
    assert b'<!DOCTYPE html>' in response.data  # Add more specific content checks as needed

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







def test_opening_times_route(client):
    # Simulate a GET request to the /opening-times route
    response = client.get('/opening-times')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected title
    assert b'<title>Opening Times</title>' in response.data
    

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