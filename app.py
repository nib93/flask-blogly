"""Blogly application."""

from flask import Flask,request,redirect,render_template
from models import db, connect_db,User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.root('/')

def root():
    """Redirect homepade to users"""
    return redirect("/users")

@app.route('/users')
def users_index():
    """Display user information"""
    users=User.query.order_by(User.first_name,User.last_name).all()
    return render_template('users/index.html',users=users)

@app.route('/users/signUp',methods=["GET"])
def user_SignUp_form():
    return render_template('users/signUp.html')

@app.route("users/signUp",method=["POST"])
def new_user_entry():
    """Create new user form and then submit"""
    new_user=User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url' or None]
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")

@app.route('/users/<int:user_id>')
def users_display(user_id):
    """Display user deatail using """
    user = User.query.get_or_404(user_id)
    return render_template('users/DisplayUser.html', user=user)


@app.route('/users/<int:user_id>/editUser')
def users_edit(user_id):
    """Edit existing user"""
    user = User.query.get_or_404(user_id)
    return render_template('users/editUser.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Update user information and submit"""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_delete(user_id):
    """Delete user information and submit"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")