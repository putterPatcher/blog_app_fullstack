from utils.connect import app, flask
from routes.home import home_blueprint
from routes.admin import admin_blueprint
from routes.blog import blog_blueprint
from utils.functions import setErrorResponse
from models.test import Test
from paths import Paths

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


app.register_blueprint(admin_blueprint, url_prefix=Paths.admin)
app.register_blueprint(blog_blueprint, url_prefix=Paths.blog)
app.register_blueprint(home_blueprint, url_prefix=Paths.home)

if __name__ == "__main__":
    app.run(debug=True)