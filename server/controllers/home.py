from utils.connect import app, collection, flask
from flask import Request

def getBlogs(request: Request):
    print("1. Entered getBlogs")

    print("TYPE OF COLLECTION:", type(collection))
    print(collection.database.client.server_info())

    cursor = collection.find({})
    print("2. Cursor created:", cursor)


    records = list(cursor)
    print("3. Records:", records)

    data = { "blogs": records }
    print("4. Data prepared")

    response = app.response_class(
        response=flask.json.dumps(data),
        status=200,
        headers={
            "Content-Type": "application/json",
        }
    )
    return response;