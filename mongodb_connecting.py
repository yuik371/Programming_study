# MongoDB_Connecting.py
from pymongo import MongoClient, errors

def get_mongo_data():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['car_recalls']
        collection = db['recalls']
        mongo_data = list(collection.find({}, {'_id': False}))  # Exclude _id field
        return mongo_data
    except errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return []
