from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
  return render_template('main-templates/home.html')

@main.route("/volunteer")
def volunteer():
  return render_template('main-templates/volunteer.html')