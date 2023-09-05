from flask import render_template, request, redirect, url_for, session
from sqlalchemy import desc
from application import app, db, bcrypt
from application.models import User, Movies, Comments, Genres, MovieGenres, Actors, MovieActors, Directors, MovieDirectors, Cart
from application.forms import SignUpForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
                # check if user has a cart
                cart = Cart.query.filter_by(user_id=user.id).first()
                if cart:
                    print('cart found')
                else:
                    print('cart not found')
                    cart = Cart(user_id=user.id)
                    db.session.add(cart)
                    db.session.commit()
                return render_template('home.html', title='Home', message="Login Successful!")
            else:
                print('user not found')
                message = 'Login Unsuccessful. Please check email and password'
        else:
            print('not validated')
    return render_template('/login.html', title='Login', form=form, message=message)

<<<<<<< HEAD
@app.route('/movies')
def movies():
    movies = Movies.query.order_by(Movies.title).all()
    return render_template('movies.html', title='Movies', movies=movies)
=======
@app.route('/logout')
def clear_variable():
    session.pop('user_id', None)  # Remove 'user_id' from session
    print("Session variable cleared!")
    return redirect(url_for('home'))
>>>>>>> main
