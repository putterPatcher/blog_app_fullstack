from utils.connect import app, collection, flask
from paths import Paths


@app.route(Paths.home, methods=["GET"])
def getBlogs():
    records = collection.find({})
    data = { "blogs": records.to_list() }
    response = app.response_class(
        response=flask.json.dumps(data),
        status=200,
        headers={
            "Content-Type": "application/json",
        }
    )
    return response;