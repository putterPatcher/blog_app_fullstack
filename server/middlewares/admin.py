from utils.connect import flask, app
import utils.middleware.get_functions as get_functions

def verify_admin(func):
    def fun():
        try:
            request = flask.request
            data = request.get_json()
            print(app.config["ADMIN_TOKEN"])
            if app.config["ADMIN_LOGGED_IN"] == True:
                if data["token"] == app.config["ADMIN_TOKEN"]:
                    func()
                else:
                    raise Exception("Invalid token.")
            else:
                raise Exception("Not logged in.")
        except Exception as err:
            return app.response_class(
                response=flask.json.dumps({"success": False, "message": "Invalid credientials", "error": str(err)}),
                status=201,
                headers={
                    "Content-Type": "application/json"
                }
            )
    # verify_admin_iter is the iterator that returns the middleware function
    return next(get_functions.verify_admin_iter)
    