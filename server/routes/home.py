from utils.connect import app, flask
from paths import HomePaths
from controllers.home import *

home_blueprint = flask.Blueprint('home_blueprint', __name__)

@home_blueprint.route(HomePaths.get_blogs, methods=["GET"])
def get_blogs():return getBlogs(flask.request)
