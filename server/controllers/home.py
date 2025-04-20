from utils.connect import app, collection, flask

def getBlogs(request):
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