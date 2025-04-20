from utils.connect import app, flask, collection
from uuid import uuid4

def login(request: flask.Request):
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

def logout(request: flask.Request, **kwargs):
    try:
        print(request.user)
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

def addBlog(request: flask.Request):
    request = flask.request
    data = request.get_json()
    collection.insert_one(data)
    return app.response_class(
        response=flask.json.dumps({"success": True})        
    )

def updateBlog():
    pass

def deleteBlog():
    pass