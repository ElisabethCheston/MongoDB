import os
import pymongo
if os.path.exists("env.py"):
    import env


    MONGO_URI = os.environ.get("MONGO_URI")
    DATABASE = "myFirstMongoDB"
    COLLECTION = "celebrities"


    def mongo_connect(url):
        try:
            conn = pymongo.MongoClient(url)
            print("Mongo is connected")
            return conn
except pymongo.error.ConnectionFailure as e:
    print ("Could not connect to MongoDB: %") % e


conn = mongo_connect(MONGO_URI)

coll = conn(DATABASE)[COLLECTION]

coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)