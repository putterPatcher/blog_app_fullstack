from routes import admin, blog, home
from utils.connect import app, flask
from utils.functions import setErrorResponse

setErrorResponse(
    app.response_class(
    response=flask.json.dumps({"success": False, "message": "Request failed.", "error": "Internal server error."}),
    status=500,
    headers={
        "Content-Type": "application/json"
        }
    )
)