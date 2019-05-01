from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from reely_app import db, bcrypt
from reely_app.models import User
from reely_app.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)



@users.route('/signup', methods=['GET', 'POST'])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created. Welcome to Reely!')
    return redirect(url_for('users.signin'))
  return render_template('user-templates/register.html', form=form)




@users.route('/signin', methods=['GET', 'POST'])
def signin():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.home'))
    else:
      flash('Login Unsuccessful. Please check email and password', 'danger')
  return render_template('user-templates/login.html', form=form)




@users.route('/signout')
def signout():
  logout_user()
  return redirect(url_for('users.signin'))




@users.route('/account')
def account():
  return render_template('user-templates/account.html')