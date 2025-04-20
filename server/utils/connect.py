import flask
import pymongo
import utils.config as conf

app = flask.Flask(__name__);
app.config.from_object(conf.Config())
client = pymongo.MongoClient(app.config["MONGO_DB_URI"]);
print("Connected to MongoDB.")
database = client.shank_blog;
collection = database.blogs;
