from utils.connect import app, flask
from controllers import blog
from paths import BlogPaths

@app.route(BlogPaths.get_blog, methods=["GET"])
def get_blog():return blog.getBlog(flask.request, id=id)

