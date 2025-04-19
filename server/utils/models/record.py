import pymongo
from model import Model

class Record:
    def __init__(self, Model: Model, collection: pymongo.Collection):
        if not Model.get_schema():
            print("Please run Model_Class.generate().")
        self.__Model = Model
        self.__collection = collection