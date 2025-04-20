from utils.connect import app, flask, collection
from uuid import uuid4
from paths import AdminPaths
from middlewares.admin import verify_admin
from utils.functions import run_middlewares

@app.route(AdminPaths.login, methods=["POST"])
def login():
    try:
        request = flask.request
        data = request.get_json()
        if app.config["ADMIN_NAME"] == data["name"] and (app.config["ADMIN_PASSWORD"]) == data["password"]:
            app.config.update(
                ADMIN_LOGGED_IN=True,
                ADMIN_TOKEN=uuid4().hex
            )
            return app.response_class(
                response=flask.json.dumps({"success": True, "message": "Valid credientials.", "token": app.config["ADMIN_TOKEN"]}),
                status=200,
                headers={
                    "Content-Type": "application/json",
                }
            )
        else:
            return app.response_class(
                response=flask.json.dumps({"success": False, "message": "Invalid credientials."}),
                status=401,
                headers={
                    "Content-Type": "application/json",
                }
            )
    except Exception as err:
        return app.response_class(
            response=flask.json.dumps({"success": False, "message": "Internal Server Error.", "error": str(err)}),
            status=500,
            headers={
                "Content-Type": "application/json",
            }
        )

@app.route(AdminPaths.logout, methods=["POST"])
def logout():
    try:
        if res:=run_middlewares(verify_admin()):
            return res
        print(flask.request.user, "???")
        app.config.update(
            ADMIN_LOGGED_IN=False,
        )
        return app.response_class(
            response=flask.json.dumps({"success": True, "message": "Logged out."}),
            status=200,
            headers={
                "Content-Type": "application/json",
            }
        )
    except Exception as err:
        return app.response_class(
            response=flask.json.dumps({"success": False, "message": "Internal Server Error.", "error": str(err)}),
            status=500,
            headers={
                "Content-Type": "application/json",
            }
        )

@app.route(AdminPaths.add_blog, methods=["POST"])
def addBlog():
    if res:=run_middlewares(verify_admin()):
        return res
    request = flask.request
    data = request.get_json()
    collection.insert_one(data)
    return app.response_class(
        response=flask.json.dumps({"success": True})        
    )

@app.route(AdminPaths.update_blog, methods=["POST"])
def updateBlog():
    pass

@app.route(AdminPaths.delete_blog, methods=["POST"])
def deleteBlog():
    pass