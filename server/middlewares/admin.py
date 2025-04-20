from utils.connect import flask, app

def verify_admin():
    try:
        request = flask.request
        data = request.get_json()
        print(app.config["ADMIN_TOKEN"])
        if app.config["ADMIN_LOGGED_IN"] == True:
            if data["token"] != app.config["ADMIN_TOKEN"]:
                raise Exception("Invalid token.")
        else:
            raise Exception("Not logged in.")
        request.user = {"name": app.config["ADMIN_NAME"]}
    except Exception as err:
        return app.response_class(
            response=flask.json.dumps({"success": False, "message": "Invalid credientials", "error": str(err)}),
            status=201,
            headers={
                "Content-Type": "application/json"
            }
        )
    