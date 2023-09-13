from app import app
from application import db, bcrypt
from application.models import User, Movies, MovieGenres, Genres, MovieActors, Actors, PaymentDetails, Showings, Bookings, Comments, CommentThread, MovieDirectors, Directors, Showings, Cart, CartItem, TicketType

with app.app_context():
    db.drop_all()
    db.create_all()

    # create a user
    user1 = User(name="james", email="james@qa.com", password=bcrypt.generate_password_hash("123"))
    admin1 = User(name="admin", email="admin@qa.com", password=bcrypt.generate_password_hash("123"), admin=True)

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
    actor13 = Actors(actor="Cillian Murphy")

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
    actress13 = Actors(actor="Margot Robbie")
    actress14 = Actors(actor="Florence Pugh")

    actor14 = Actors(actor="Ryan Gosling")
    actor15 = Actors(actor="Will Ferrell")

    # create a movie director
    director1 = Directors(director="Christopher Nolan")
    director2 = Directors(director="Steven Spielberg")
    director3 = Directors(director="Martin Scorsese")
    director4 = Directors(director="Quentin Tarantino")
    director5 = Directors(director="James Cameron")
    director6 = Directors(director="David Fincher")
    director7 = Directors(director="Ridley Scott")
    director8 = Directors(director="Tim Burton")
    director9 = Directors(director="Clint Eastwood")
    director10 = Directors(director="Peter Jackson")
    director11 = Directors(director="Guy Ritchie")
    director12 = Directors(director="Ron Howard")
    director13 = Directors(director="Greta Gerwig")

    # create a movie
    movie1 = Movies(title="Mission Impossible", description="A secret agent is sent to Sydney, to find and destroy a genetically modified disease called 'Chimera'.", image="images/mission_impossible.jpeg", release_date="1996-05-22")
    movie1_genre = MovieGenres(movie_id=1, genre_id=1)
    movie1_actor_1 = MovieActors(movie_id=1, actor_id=1)
    movie1_actor_2 = MovieActors(movie_id=1, actor_id=2)
    movie1_actor_3 = MovieActors(movie_id=1, actor_id=3)
    movie1_director = MovieDirectors(movie_id=1, director_id=1)


    movie2 = Movies(title="The Matrix", description="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",  image="images/the_matrix.jpg", release_date="1999-03-31")
    movie2_genre = MovieGenres(movie_id=2, genre_id=5)
    movie2_actor_1 = MovieActors(movie_id=2, actor_id=3)
    movie2_actor_2 = MovieActors(movie_id=2, actor_id=4)
    movie2_actor_3 = MovieActors(movie_id=2, actor_id=5)
    movie2_director = MovieDirectors(movie_id=2, director_id=5)

    movie3 = Movies(title="The Dark Knight", description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.", image="images/the_dark_knight.jpg", release_date="2008-07-14")
    movie3_genre = MovieGenres(movie_id=3, genre_id=1)
    movie3_actor_1 = MovieActors(movie_id=3, actor_id=5)
    movie3_actor_2 = MovieActors(movie_id=3, actor_id=6)
    movie3_actor_3 = MovieActors(movie_id=3, actor_id=7)
    movie3_director = MovieDirectors(movie_id=3, director_id=1)

    movie4 = Movies(title="The Godfather", description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", image="images/the_godfather.jpg", release_date="1972-03-24")
    movie4_genre = MovieGenres(movie_id=4, genre_id=10)
    movie4_actor_1 = MovieActors(movie_id=4, actor_id=8)
    movie4_actor_2 = MovieActors(movie_id=4, actor_id=9)
    movie4_actor_3 = MovieActors(movie_id=4, actor_id=10)
    movie4_director = MovieDirectors(movie_id=4, director_id=3)

    new_release1 = Movies(title="Oppenheimer", description="A look at the life of J. Robert Oppenheimer, the physicist tasked with developing the first atomic bomb.", image="images/oppenheimer.jpeg", release_date="2023-07-21")
    new_release1_genre = MovieGenres(movie_id=5, genre_id=13)
    new_release1_actor_1 = MovieActors(movie_id=5, actor_id=5)
    new_release1_actor_2 = MovieActors(movie_id=5, actor_id=13)
    new_release1_actor_3 = MovieActors(movie_id=5, actor_id=27)
    new_release1_director = MovieDirectors(movie_id=5, director_id=1)

    new_release2 = Movies(title="Barbie", description="Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.", image="images/barbie.jpeg", release_date="2023-07-21")
    new_release2_genre = MovieGenres(movie_id=6, genre_id=2)
    new_release2_genre_2 = MovieGenres(movie_id=6, genre_id=8)
    new_release2_actor_1 = MovieActors(movie_id=6, actor_id=26)
    new_release2_actor_2 = MovieActors(movie_id=6, actor_id=28)
    new_release2_actor_3 = MovieActors(movie_id=6, actor_id=29)
    new_release2_director = MovieDirectors(movie_id=6, director_id=13)

    showing1 = Showings(movie_id=1, screen_number=1, date="2023-10-01 12:00:00", seats_available=10)
    showing2 = Showings(movie_id=1, screen_number=1, date="2023-10-01 15:00:00", seats_available=100)
    showing3 = Showings(movie_id=1, screen_number=2, date="2023-10-01 18:00:00", seats_available=100)
    showing4 = Showings(movie_id=1, screen_number=2, date="2023-10-01 21:00:00", seats_available=100)

    showing5 = Showings(movie_id=2, screen_number=5, date="2023-10-11 12:00:00", seats_available=100)
    showing6 = Showings(movie_id=2, screen_number=5, date="2023-10-11 15:00:00", seats_available=100)
    showing7 = Showings(movie_id=2, screen_number=6, date="2023-10-11 18:00:00", seats_available=100)
    showing8 = Showings(movie_id=2, screen_number=6, date="2023-10-11 21:00:00", seats_available=100)

    showing9 = Showings(movie_id=3, screen_number=9, date="2023-10-21 12:00:00", seats_available=100)
    showing10 = Showings(movie_id=3, screen_number=9, date="2023-10-21 15:00:00", seats_available=100)
    showing11 = Showings(movie_id=3, screen_number=10, date="2023-10-21 18:00:00", seats_available=100)
    showing12 = Showings(movie_id=3, screen_number=10, date="2023-10-21 21:00:00", seats_available=100)

    showing13 = Showings(movie_id=4, screen_number=13, date="2023-10-31 12:00:00", seats_available=100)
    showing14 = Showings(movie_id=4, screen_number=13, date="2023-10-31 15:00:00", seats_available=100)
    showing15 = Showings(movie_id=4, screen_number=14, date="2023-10-31 18:00:00", seats_available=100)
    showing16 = Showings(movie_id=4, screen_number=14, date="2023-10-31 21:00:00", seats_available=100)

    showing17 = Showings(movie_id=5, screen_number=17, date="2023-11-01 12:00:00", seats_available=100)
    showing18 = Showings(movie_id=5, screen_number=17, date="2023-11-01 15:00:00", seats_available=100)
    showing19 = Showings(movie_id=5, screen_number=18, date="2023-11-01 18:00:00", seats_available=100)
    showing20 = Showings(movie_id=5, screen_number=18, date="2023-11-01 21:00:00", seats_available=100)

    showing21 = Showings(movie_id=6, screen_number=21, date="2023-11-11 12:00:00", seats_available=100)
    showing22 = Showings(movie_id=6, screen_number=21, date="2023-11-11 15:00:00", seats_available=100)
    showing23 = Showings(movie_id=6, screen_number=22, date="2023-11-11 18:00:00", seats_available=100)
    showing24 = Showings(movie_id=6, screen_number=22, date="2023-11-11 21:00:00", seats_available=100)








    adult_ticket_type = TicketType(ticket_type="Adult", price=10)
    child_ticket_type = TicketType(ticket_type="Child", price=5)

    # create a comment thread
    comment_thread1 = CommentThread(title="Mission Impossible")
    comment_thread2 = CommentThread(title="The Matrix")
    comment_thread3 = CommentThread(title="The Dark Knight")
    comment_thread4 = CommentThread(title="The Godfather")

    

    comment1 = Comments(comment_thread_id=1, user_id=1, comment="This is a comment")
    comment2 = Comments(comment_thread_id=1, user_id=1, comment="This is another comment")
    comment3 = Comments(comment_thread_id=1, user_id=1, comment="This is a third comment")

    # add everything to the database
    db.session.add(genre1)
    db.session.add(genre2)
    db.session.add(genre3)
    db.session.add(genre4)
    db.session.add(genre5)
    db.session.add(genre6)
    db.session.add(genre7)
    db.session.add(genre8)
    db.session.add(genre9)
    db.session.add(genre10)
    db.session.add(genre11)
    db.session.add(genre12)
    db.session.add(genre13)
    db.session.add(genre14)
    db.session.add(genre15)
    db.session.add(genre16)
    db.session.add(genre17)
    db.session.add(genre18)
    db.session.add(genre19)
    db.session.add(genre20)
    db.session.add(genre21)

    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(actor3)
    db.session.add(actor4)
    db.session.add(actor5)
    db.session.add(actor6)
    db.session.add(actor7)
    db.session.add(actor8)
    db.session.add(actor9)
    db.session.add(actor10)
    db.session.add(actor11)
    db.session.add(actor12)
    db.session.add(actor13)
    
    db.session.add(actress1)
    db.session.add(actress2)
    db.session.add(actress3)
    db.session.add(actress4)
    db.session.add(actress5)
    db.session.add(actress6)
    db.session.add(actress7)
    db.session.add(actress8)
    db.session.add(actress9)
    db.session.add(actress10)
    db.session.add(actress11)
    db.session.add(actress12)
    db.session.add(actress13)
    db.session.add(actress14)

    db.session.add(actor14)
    db.session.add(actor15)

    
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(director4)
    db.session.add(director5)
    db.session.add(director6)
    db.session.add(director7)
    db.session.add(director8)
    db.session.add(director9)
    db.session.add(director10)
    db.session.add(director11)
    db.session.add(director12)
    db.session.add(director13)

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.add(new_release1)
    db.session.add(new_release2)
    db.session.commit()

    db.session.add(movie1_genre)
    db.session.add(movie1_actor_1)
    db.session.add(movie1_actor_2)
    db.session.add(movie1_actor_3)
    db.session.add(movie1_director)

    db.session.add(movie2_genre)
    db.session.add(movie2_actor_1)
    db.session.add(movie2_actor_2)
    db.session.add(movie2_actor_3)
    db.session.add(movie2_director)

    db.session.add(movie3_genre)
    db.session.add(movie3_actor_1)
    db.session.add(movie3_actor_2)
    db.session.add(movie3_actor_3)
    db.session.add(movie3_director)

    db.session.add(movie4_genre)
    db.session.add(movie4_actor_1)
    db.session.add(movie4_actor_2)
    db.session.add(movie4_actor_3)
    db.session.add(movie4_director)

    db.session.add(new_release1_genre)
    db.session.add(new_release1_actor_1)
    db.session.add(new_release1_actor_2)
    db.session.add(new_release1_actor_3)
    db.session.add(new_release1_director)

    db.session.add(new_release2_genre)
    db.session.add(new_release2_genre_2)
    db.session.add(new_release2_actor_1)
    db.session.add(new_release2_actor_2)
    db.session.add(new_release2_actor_3)
    db.session.add(new_release2_director)




    db.session.add(comment_thread1)
    db.session.add(comment_thread2)
    db.session.add(comment_thread3)
    db.session.add(comment_thread4)

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)


    db.session.add(user1)
    db.session.add(admin1)

    db.session.add(showing1)
    db.session.add(showing2)
    db.session.add(showing3)
    db.session.add(showing4)
    db.session.add(showing5)
    db.session.add(showing6)
    db.session.add(showing7)
    db.session.add(showing8)
    db.session.add(showing9)
    db.session.add(showing10)
    db.session.add(showing11)
    db.session.add(showing12)
    db.session.add(showing13)
    db.session.add(showing14)
    db.session.add(showing15)
    db.session.add(showing16)
    db.session.add(showing17)
    db.session.add(showing18)
    db.session.add(showing19)
    db.session.add(showing20)
    db.session.add(showing21)
    db.session.add(showing22)
    db.session.add(showing23)
    db.session.add(showing24)


    db.session.add(adult_ticket_type)
    db.session.add(child_ticket_type)


    db.session.commit()
    