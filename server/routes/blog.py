from utils.connect import app, flask
from paths import BlogPaths
from controllers import blog

@app.route(BlogPaths.get_blog, methods=["GET"])
def get_blog(id):
    request = flask.request
    return blog.getBlog(request, id)
