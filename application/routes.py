from flask import render_template, request, redirect, url_for, session
from sqlalchemy import desc
from application import app, db

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')
