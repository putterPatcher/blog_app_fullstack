from utils.connect import app, collection, flask
from models.blog import Blog

def getBlog(request, id):
    record = collection.find_one({"_id": id})
    if record:
        data = { "blog": record }
        response = app.response_class(
            response=flask.json.dumps(data),
            status=200,
            headers={
                "Content-Type": "application/json",
            }
        )
    else:
        response = app.response_class(
            response=flask.json.dumps({
                "success": "false",
                "error": "Blog does not exist."
            }),
            status=500,
            headers={
                "Content-Type": "application/json",
            }
        )
    return response;