from utils.connect import app, flask
from paths import AdminPaths
from controllers import admin
from middlewares.admin import verify_admin

@app.route(AdminPaths.login, methods=["POST"])
def login():
    request = flask.request
    return admin.login(request)

@app.route(AdminPaths.logout, methods=["POST"])
def logout():
    request = flask.request
    return verify_admin(request, admin.logout)

@app.route(AdminPaths.add_blog, methods=["POST"])
def add_blog():
    request = flask.request
    return verify_admin(request, admin.addBlog)

@app.route(AdminPaths.update_blog, methods=["POST"])
def update_blog():
    request = flask.request
    return verify_admin(request, admin.updateBlog)

@app.route(AdminPaths.delete_blog, methods=["POST"])
def delete_blog():
    request = flask.request
    return verify_admin(request, admin.deleteBlog)

