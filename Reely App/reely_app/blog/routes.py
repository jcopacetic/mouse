from flask import Blueprint, render_template
from reely_app.models import Posts

blog = Blueprint('blog', __name__)

@blog.route("/tutorials")
def tutorials():
  posts = Posts
  return render_template('blog-templates/posts-list.html', posts=posts)

@blog.route("/tutorials/<string:whatever>")
def tutorial(whatever):
  return render_template('blog-templates/individual-post.html')