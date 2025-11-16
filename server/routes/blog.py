from utils.connect import app, flask
from controllers.blog import *
from paths import BlogPaths

blog_blueprint = flask.Blueprint('blog_blueprint', __name__)

@blog_blueprint.route(BlogPaths.get_blog, methods=["GET"])
def get_blog(id):return getBlog(flask.request, id=id)

