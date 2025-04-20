from utils.connect import app, collection, flask
from flask import Request
from paths import Paths

def getBlogs(request: Request):
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