from flask import render_template, request, redirect, url_for, session
from sqlalchemy import desc
from application import app, db, bcrypt
from application.models import User, Movies, Comments, Genres, MovieGenres, Actors, MovieActors, Directors, MovieDirectors
from application.forms import SignUpForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

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
