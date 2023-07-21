from pymongo import MongoClient
from decouple import config

MONGO_USER = config("MONGO_USER")
MONGO_PASSWORD = config("MONGO_PASSWORD")
MONGO_DBNAME = config("MONGO_DBNAME")

mongo_client = MongoClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@localhost:27017/{MONGO_DBNAME}?authSource=admin"
)
database = mongo_client["database"]
