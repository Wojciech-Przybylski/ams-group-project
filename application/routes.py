from flask import render_template, request, redirect, url_for, session
from flask_cors import cross_origin
from sqlalchemy import desc
from application import app, db, bcrypt
from application.models import User, Movies, Comments, Genres, MovieGenres, Actors, MovieActors, Directors, MovieDirectors, Cart, CommentThread, CommentView, Showings, CartItem, TicketType, PaymentDetails, Bookings, BookingsItems
from application.forms import CreateThreadForm, SignUpForm, LoginForm, CreateCommentForm, BookingForm, PaymentForm
from datetime import datetime, timedelta

@app.route('/')
@app.route('/home')
def home():
    # get all movies from db
    movies = Movies.query.order_by(Movies.title).all()
    return render_template('home.html', title='Home', movies=movies)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if user is logged in, redirect to home page
    if 'user_id' in session:
        return redirect(url_for('home'))
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        print('validated')
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('/signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user is logged in, redirect to home page
    if 'user_id' in session:
        return redirect(url_for('home'))
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        print('post')
        if form.validate_on_submit():
            print('validated')
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                print('user found')
                # create session variable for user_id
                session['user_id'] = user.id
                # if user is admin, create session variable for admin
                # create session variable for user name
                session['user_name'] = user.name
                if user.admin:
                    session['admin'] = True
                # check if user has a cart
                cart = Cart.query.filter_by(user_id=user.id).first()
                if cart:
                    print('cart found')
                else:
                    print('cart not found')
                    cart = Cart(user_id=user.id)
                    db.session.add(cart)
                    db.session.commit()
                return redirect(url_for('home'))
            else:
                print('user not found')
                message = 'Login Unsuccessful. Please check email and password'
        else:
            print('not validated')
    return render_template('/login.html', title='Login', form=form, message=message)

@app.route('/movies')
def movies():
    movies = Movies.query.order_by(Movies.title).all()
    return render_template('movies.html', title='Movies', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = Movies.query.get(movie_id)
    #  get genre from movie_genres
    genres = MovieGenres.query.filter_by(movie_id=movie_id).all()
    # get showings from db
    showings = Showings.query.filter_by(movie_id=movie_id).all()
    #  get genre name from genres
    genre_names = []
    for genre in genres:
        genre_names.append(Genres.query.get(genre.genre_id).genre)
    #  get actor from movie_actors
    actors = MovieActors.query.filter_by(movie_id=movie_id).all()
    #  get actor name from actors
    actor_names = []
    for actor in actors:
        actor_names.append(Actors.query.get(actor.actor_id).actor)
    #  get director from movie_directors
    directors = MovieDirectors.query.filter_by(movie_id=movie_id).all()
    #  get director name from directors
    director_names = []
    for director in directors:
        director_names.append(Directors.query.get(director.director_id).director)
    return render_template('movie.html', title=movie.title, movie=movie, genre_names=genre_names, actor_names=actor_names, director_names=director_names, showings=showings)

@app.route('/new-releases')
def new_releases():
    # movies = Movies.query.order_by(Movies.title).all()
    # get all movies from db if they are less than 3 months old
    movies = Movies.query.filter(Movies.release_date >= datetime.utcnow() - timedelta(days=90)).order_by(Movies.release_date).all()
    return render_template('movies.html', title='Movies', movies=movies)

@app.route('/logout')
def clear_variable():
    session.pop('user_id', None)  # Remove 'user_id' from session
    session.pop('admin', None)  # Remove 'admin' from session
    session.pop('user_name', None)  # Remove 'user_name' from session
    print("Session variable cleared!")
    return redirect(url_for('home'))

@app.route('/discussion-board', methods=['GET', 'POST'])
def discussion_board():
    # if method is post, add thread to db
    if request.method == 'POST':
        title = request.form.get('title')
        comment_thread = CommentThread(title=title)
        db.session.add(comment_thread)
        db.session.commit()
        return redirect(url_for('discussion_board'))
    # if user is not logged in, redirect to login page
    if 'user_id' not in session:
        return redirect(url_for('login'))
    new_thread_form = CreateThreadForm()
    comment_threads = CommentThread.query.order_by(desc(CommentThread.id)).all()
    return render_template('discussion-board.html', title='Discussion Board', comment_threads=comment_threads, form=new_thread_form)

@app.route('/discussion-board/<int:thread_id>', methods=['GET', 'POST'])
def thread(thread_id):

    # if method is post, add comment to db
    if request.method == 'POST':
        comment = request.form.get('comment')
        user_id = session['user_id']
        new_comment = Comments(comment_thread_id=thread_id, user_id=user_id, comment=comment, date=datetime.utcnow())
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('thread', thread_id=thread_id))
    # if user is not logged in, redirect to login page
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # create comment form
    form = CreateCommentForm()
    # get thread from db
    thread = CommentThread.query.get(thread_id)
    # get comments from db
    comments = Comments.query.filter_by(comment_thread_id=thread_id).order_by(desc(Comments.id)).all()
    comment_view_list = []
    for comment in comments:
        comment_view = CommentView(id=comment.id, comment=comment.comment, user_name=User.query.get(comment.user_id).name, time=comment.date.strftime("%d/%m/%Y %H:%M:%S"))
        comment_view_list.append(comment_view)

    return render_template('thread.html', thread=thread, comments=comment_view_list, form=form)

@app.route('/delete-comment/<int:comment_id>', methods=['GET', 'POST'])
def delete_comment(comment_id):
    # get comment from db
    comment = Comments.query.get(comment_id)
    # get thread id from comment
    thread_id = comment.comment_thread_id
    # delete comment from db
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('thread', thread_id=thread_id))


@app.route('/opening-times')
def opening_times():
    return render_template('opening-times.html', title='Opening Times')

@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])
def book_tickets(movie_id):
    # if user is not logged in, redirect to login page
    if 'user_id' not in session:
        return redirect(url_for('login'))
    else:
        # get users name
        user = User.query.get(session['user_id'])
        # get users cart
        cart = Cart.query.filter_by(user_id=session['user_id']).first()
        # create booking form
        form = BookingForm()
        # get movie info
        movie = Movies.query.get(movie_id)
        # get all showings for movie
        showings = Showings.query.filter_by(movie_id=movie_id).all()
        choices = []
        for showing in showings:
            choices.append((showing.id, showing.date.strftime("%d/%m/%Y %H:%M:%S")))
        form.showing_id.choices = choices
        # if method is post, add tickets to cart
        if request.method == 'POST' and form.validate_on_submit():
            # get form data
            showing_id = request.form.get('showing_id')
            child_tickets = request.form.get('child_tickets')
            adult_tickets = request.form.get('adult_tickets')
            quantity = request.form.get('quantity')
            # create cart items only if quantity is greater than 0
            if int(child_tickets) != 0:
                child_cart_item = CartItem(showing_id=showing_id, ticket_type_id=1, quantity=child_tickets, cart_id=cart.id)
                db.session.add(child_cart_item)
            if int(adult_tickets) != 0:
                adult_cart_item = CartItem(showing_id=showing_id, ticket_type_id=2, quantity=adult_tickets, cart_id=cart.id)
                db.session.add(adult_cart_item)
            db.session.commit()
            # redirect to payment page only if either quantity is greater than 0
            if int(child_tickets) != 0 or int(adult_tickets)!= 0:
                return redirect(url_for('payment'))
        return render_template('book.html', title='Book Tickets', movie=movie, showings=showings, cart=cart, form=form, name=user.name)
    
@app.route('/payment', methods=['GET', 'POST'])
def payment():
    cart = Cart.query.filter_by(user_id=session['user_id']).first()
    cart_items = CartItem.query.filter_by(cart_id=cart.id).all()
    # if user is logged in
    if 'user_id' in session:
        # if method is post
        if request.method == 'POST':
            if PaymentDetails.query.filter_by(user_id=session['user_id'], card_number=request.form['card_number']).first():
                # retrieve payment details record
                payment_details = PaymentDetails.query.filter_by(user_id=session['user_id'], card_number=request.form['card_number']).first()
            else:
                # create payment details record
                payment_details = PaymentDetails(
                    user_id = session['user_id'],
                    card_name = request.form['card_name'],
                    card_number = request.form['card_number'],
                    expiry_date = request.form['expiry_date'],
                    security_code = request.form['security_code'])
            db.session.add(payment_details)
            db.session.commit()
            # get showing id from cart
            showing_id = cart_items[0].showing_id
            # get movie id from showing
            movie_id = Showings.query.get(showing_id).movie_id
            booking = Bookings(user_id=session['user_id'], movie_id=movie_id, date=datetime.utcnow())
            db.session.add(booking)
            db.session.commit()
            # get the booking id for the booking just created
            booking = Bookings.query.filter_by(user_id=session['user_id']).order_by(desc(Bookings.id)).first()
            for item in cart_items:
                # create booking item
                booking_item = BookingsItems(
                    booking_id = booking.id,
                    showing_id = item.showing_id,
                    ticket_type_id = item.ticket_type_id,
                    quantity = item.quantity
                )
                db.session.add(booking_item)
                db.session.commit()
            # empty cart
            cart.empty_cart()
            # set quantity of tickets in viewings table based on tickets just sold
            booking_items = BookingsItems.query.filter_by(booking_id=booking.id).all()
            for item in booking_items:
                showing = Showings.query.get(item.showing_id)
                showing.seats_available -= item.quantity
                db.session.commit()
            return redirect("/confirmation/" + str(booking.id))
         # if method isn't post - load page

        # search payment_details table for user_id - sent to form for autofill option
        payment_details = PaymentDetails.query.filter_by(user_id=session['user_id']).all()
        # create from
        payment_form = PaymentForm()
        return render_template('/payment.html', title='Checkout', form=payment_form, payment_details=payment_details)
    
    else:
        return redirect(url_for('home'))
    
@app.route('/confirmation/<int:booking_id>')
def confirmation(booking_id):
    booking = Bookings.query.get(booking_id)
    booking_items = BookingsItems.query.filter_by(booking_id=booking_id).all()
    # get user name
    user = User.query.get(session['user_id'])
    # get movie name
    movie = Movies.query.get(booking.movie_id)
    return render_template('/confirmation.html', title='Confirmation', booking=booking, booking_items=booking_items, movie_name=movie.title, user_name=user.name)

@app.route('/get_remaining_tickets/<int:showing_id>')
@cross_origin(origin='*', methods=['GET', 'POST'])
def get_remaining_tickets(showing_id):
    showing = Showings.query.get(showing_id)
    return str(showing.seats_available)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form.get('search')
        return redirect(url_for('search_results', search=search))

@app.route('/search-results/<string:search>')
def search_results(search):
    movies = Movies.query.filter(Movies.title.like('%' + search + '%')).all()
    # find all movies where the actor name is like the search
    actors = Actors.query.filter(Actors.actor.like('%' + search + '%')).all()
    for actor in actors:
        # find all movies where the actor id is in the movie_actors table
        movies_with_actor = MovieActors.query.filter_by(actor_id=actor.id).all()
        for movie in movies_with_actor:
            # if the movie is not already in the movies list, add it
            if movie.movie_id not in movies:
                movies.append(Movies.query.get(movie.movie_id))
    # find all movies where the director name is like the search
    directors = Directors.query.filter(Directors.director.like('%' + search + '%')).all()
    for director in directors:
        # find all movies where the director id is in the movie_directors table
        movies_with_director = MovieDirectors.query.filter_by(director_id=director.id).all()
        for movie in movies_with_director:
            # if the movie is not already in the movies list, add it
            if movie.movie_id not in movies:
                movies.append(Movies.query.get(movie.movie_id))
    # find all movies where the genre name is like the search
    genres = Genres.query.filter(Genres.genre.like('%' + search + '%')).all()
    for genre in genres:
        # find all movies where the genre id is in the movie_genres table
        movies_with_genre = MovieGenres.query.filter_by(genre_id=genre.id).all()
        for movie in movies_with_genre:
            # if the movie is not already in the movies list, add it
            if movie.movie_id not in movies:
                movies.append(Movies.query.get(movie.movie_id))
    return render_template('search_results.html' , title=('Search results for: ' + search), movies=movies)

@app.route('/classifications')
def clasifications():
    return render_template('classifications.html', title='UK Film Classification System')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact-us')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/screens')
def screens():
    return render_template('screens.html', title='Screens')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form.get('search')
        return redirect(url_for('search_results', search=search))

@app.route('/search-results/<string:search>')
def search_results(search):
    movies = Movies.query.filter(Movies.title.like('%' + search + '%')).all()
    # find all movies where the actor name is like the search
    actors = Actors.query.filter(Actors.actor.like('%' + search + '%')).all()
    for actor in actors:
        # find all movies where the actor id is in the movie_actors table
        movies_with_actor = MovieActors.query.filter_by(actor_id=actor.id).all()
        for movie in movies_with_actor:
            # if the movie is not already in the movies list, add it
            if movie.movie_id not in movies:
                movies.append(Movies.query.get(movie.movie_id))
    # find all movies where the director name is like the search
    directors = Directors.query.filter(Directors.director.like('%' + search + '%')).all()
    for director in directors:
        # find all movies where the director id is in the movie_directors table
        movies_with_director = MovieDirectors.query.filter_by(director_id=director.id).all()
        for movie in movies_with_director:
            # if the movie is not already in the movies list, add it
            if movie.movie_id not in movies:
                movies.append(Movies.query.get(movie.movie_id))
    # find all movies where the genre name is like the search
    genres = Genres.query.filter(Genres.genre.like('%' + search + '%')).all()
    for genre in genres:
        # find all movies where the genre id is in the movie_genres table
        movies_with_genre = MovieGenres.query.filter_by(genre_id=genre.id).all()
        for movie in movies_with_genre:
            # if the movie is not already in the movies list, add it
            if movie.movie_id not in movies:
                movies.append(Movies.query.get(movie.movie_id))
    return render_template('search_results.html' , title=('Search results for: ' + search), movies=movies)

@app.route('/classifications')
def clasifications():
    return render_template('classifications.html', title='UK Film Classification System')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact-us')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/screens')
def screens():
    return render_template('screens.html', title='Screens')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404