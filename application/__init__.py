from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv
from sqlalchemy import create_engine



app = Flask(__name__)

db_password = getenv('DB_PASSWORD')

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{db_password}@172.17.0.1:3306/cinema'

def create_db_engine(db_url):
    engine = create_engine(db_url)
    return engine

db_engine = create_db_engine("postgresql://user:password@localhost/test")


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