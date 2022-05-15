"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

image_url = 'https://images.pexels.com/photos/11990061/pexels-photo-11990061.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, default=image_url)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def connect_db(app):
    db.app = app
    db.init_app(app)