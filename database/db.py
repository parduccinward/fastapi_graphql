from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017)

database = mongo_client["database"]
