from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv



app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:password@localhost:3306/cinema'

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

bcrypt = Bcrypt(app)
# this is the homepage branch!

@app.context_processor
def inject_search_form():
    search_form = SearchForm()
    return dict(search_form=search_form)

from application import routes
from application.forms import SearchForm  # Import your SearchForm