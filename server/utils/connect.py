import flask
import pymongo
import utils.config as conf

app = flask.Flask(__name__)
app.config.from_object(conf.Config())

client = pymongo.MongoClient(
    app.config["MONGO_DB_URI"]
)

try:
    client.server_info()
    print("Connected to MongoDB.")
except Exception as e:
    print("MongoDB connection error:", e)

database = client.shank_blog
collection = database.blogs