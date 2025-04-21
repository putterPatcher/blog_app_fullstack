from routes import admin, blog, home
from utils.connect import app, flask
from utils.functions import setErrorResponse
from models.test import Test

setErrorResponse(
    app.response_class(
    response=flask.json.dumps({"success": False, "message": "Request failed.", "error": "Internal server error."}),
    status=500,
    headers={
        "Content-Type": "application/json"
        }
    )
)

print(Test.compare_record({"abc": 5, 'acd': {"abc": "sdfdgb"}}, allow_extra=True))
