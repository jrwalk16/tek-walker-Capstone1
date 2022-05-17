from flask import Flask, redirect, url_for, session
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms.validators import DataRequired
from sqlalchemy import create_engine



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jonah22Milo18@localhost/tractortek'

db = SQLAlchemy(app)

class Sales(db.Model):

    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(200), nullable=False)
    employee_id = db.Column(db.String(200), nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('home.html')




@app.route('/sales')
def sales():
    return render_template('sales.html')
