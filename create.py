from app import app
from application import db, bcrypt
from application.models import User, Movies, MovieGenres, Genres, MovieActors, Actors, PaymentDetails, Showings, Bookings, Comments, CommentThread

with app.app_context():
    db.drop_all()
    db.create_all()

    # create a movie genre
    genre1 = Genres(genre="Action")
    genre2 = Genres(genre="Comedy")
    genre3 = Genres(genre="Horror")
    genre4 = Genres(genre="Romance")
    genre5 = Genres(genre="Sci-Fi")
    genre6 = Genres(genre="Thriller")
    genre7 = Genres(genre="Western")
    genre8 = Genres(genre="Drama")
    genre9 = Genres(genre="Fantasy")
    genre10 = Genres(genre="Crime")
    genre11 = Genres(genre="Adventure")
    genre12 = Genres(genre="Animation")
    genre13 = Genres(genre="Biography")
    genre14 = Genres(genre="Documentary")
    genre15 = Genres(genre="Family")
    genre16 = Genres(genre="History")
    genre17 = Genres(genre="Music")
    genre18 = Genres(genre="Musical")
    genre19 = Genres(genre="Mystery")
    genre20 = Genres(genre="Sport")
    genre21 = Genres(genre="War")

    # create a movie actor
    actor1 = Actors(actor="Tom Cruise")
    actor2 = Actors(actor="Brad Pitt")
    actor3 = Actors(actor="Leonardo DiCaprio")
    actor4 = Actors(actor="Will Smith")
    actor5 = Actors(actor="Robert Downey Jr.")
    actor6 = Actors(actor="Tom Hanks")
    actor7 = Actors(actor="Dwayne Johnson")
    actor8 = Actors(actor="Samuel L. Jackson")
    actor9 = Actors(actor="Johnny Depp")
    actor10 = Actors(actor="Matt Damon")
    actor11 = Actors(actor="Harrison Ford")
    actor12 = Actors(actor="Morgan Freeman")

    #  create a movie actress
    actress1 = Actors(actor="Scarlett Johansson")
    actress2 = Actors(actor="Jennifer Lawrence")
    actress3 = Actors(actor="Jennifer Aniston")
    actress4 = Actors(actor="Angelina Jolie")
    actress5 = Actors(actor="Emma Stone")
    actress6 = Actors(actor="Anne Hathaway")
    actress7 = Actors(actor="Sandra Bullock")
    actress8 = Actors(actor="Julia Roberts")
    actress9 = Actors(actor="Mila Kunis")
    actress10 = Actors(actor="Charlize Theron")
    actress11 = Actors(actor="Natalie Portman")
    actress12 = Actors(actor="Meryl Streep")

    # create a movie
    movie1 = Movies(title="Mission Impossible", )