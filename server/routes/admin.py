from utils.connect import app, flask
from controllers import admin
from paths import AdminPaths
from utils.functions import get_response
from middlewares import admin as adminMiddleware

admin_blueprint = flask.Blueprint('admin_blueprint', __name__)

@admin_blueprint.route(AdminPaths.login, methods=["POST"])
def login():return admin.login(flask.request)

@admin_blueprint.route(AdminPaths.logout, methods=["POST"])
def logout():return get_response(flask.request, admin.logout, adminMiddleware.verify_admin)

@admin_blueprint.route(AdminPaths.add_blog, methods=["POST"])
def add_blog():return get_response(flask.request, admin.addBlog, adminMiddleware.verify_admin)

@admin_blueprint.route(AdminPaths.update_blog, methods=["POST"])
def update_blog(id):return get_response(flask.request, admin.updateBlog, adminMiddleware.verify_admin, id=id)

@admin_blueprint.route(AdminPaths.delete_blog, methods=["POST"])
def delete_blog(id):return get_response(flask.request, admin.deleteBlog, adminMiddleware.verify_admin, id=id)
