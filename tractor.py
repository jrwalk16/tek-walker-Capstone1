from flask import Flask, redirect, url_for, session
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms.validators import DataRequired
from sqlalchemy import create_engine



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jonah22Milo18@localhost/tractortek'
app.config['SECRET_KEY'] = "my super secret key"

db = SQLAlchemy(app)

class Sales(db.Model):

    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(200), nullable=False)
    employee_id = db.Column(db.String(200), nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    week = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name


class DbSalesForm(FlaskForm):
    product_id = StringField("Product number", validators=[DataRequired()])
    employee_id = StringField("Employee number", validators=[DataRequired()])
    quantity_sold = IntegerField("Quantity sold", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()]) 
    week = IntegerField("Week", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template('home.html')




@app.route('/sales', methods=['POST', 'GET'])
def sales():
    product_id = None
    employee_id = None
    quantity_sold = None
    year = None
    week = None
    form = DbSalesForm()
    if form.validate_on_submit():
        sales = Sales(product_id=form.product_id.data, employee_id=form.employee_id.data, quantity_sold=form.quantity_sold.data, year=form.year.data, week=form.week.data)
        db.session.add(sales)
        db.session.commit()
    product_id = form.product_id.data
    employee_id = form.employee_id.data
    quantity_sold = form.quantity_sold.data
    year = form.year.data
    week = form.year.data
    form.product_id.data = ''
    form.employee_id.data = ''
    form.quantity_sold.data = ''
    form.year.data = ''
    form.week.data = ''

    return render_template('sales.html', form=form, product_id=product_id, employee_id=employee_id, quantity_sold=quantity_sold, year=year, week=week)
