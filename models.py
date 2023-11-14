"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
class User(db.Model):
    """Create user table"""
    __tablename__="users"

    """create database columns"""
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.Text, nullable=False)
    last_name=db.Column(db.Text,nullable=False)
    image_url=db.column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    """return first name and last name of the user"""
    def user_name(self):
        return f"{self.first_name}{self.last_name}"

"""Connect database to flask"""
def connect_db(app):
    db.app=app
    db.init_app(app)