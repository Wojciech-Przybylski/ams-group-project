from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/flask_test"

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

bcrypt = Bcrypt(app)


from application import routes