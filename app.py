"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretCode'

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/users')
def users_list():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('index.html', users=users)

@app.route('/new-user', methods=['GET'])
def new_user():
    return render_template('new-user.html')

@app.route('/add-users', methods=['POST'])
def adding_users():
    user = User(
        first_name=request.form['first'], 
        last_name=request.form['last'], 
        image=request.form['img_url']
    )
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('user-profile.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get(user_id)
    return render_template('edit-user.html', user=user)

@app.route('/users/<int:user_id>/edit-user', methods=['POST'])
def submit_edit(user_id):
    user = User.query.get(user_id)

    user.first_name = request.form['first']
    user.last_name = request.form['last']
    user.image = request.form['img_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')


