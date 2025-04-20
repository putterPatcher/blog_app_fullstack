from utils.connect import app, flask
from paths import HomePaths
from controllers import home

@app.route(HomePaths.get_blogs, methods=["GET"])
def get_blogs():
    request = flask.request
    return home.getBlogs(request)