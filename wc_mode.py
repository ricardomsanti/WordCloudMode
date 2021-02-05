from pymongo import MongoClient

#client
client = MongoClient("localhost",27017)
#database
db = client.get_database("test")
#collection
word_cloud = db.get_collection("word_cloud")
#collection operations
for x in word_cloud.find({},{ "_id":0, "field":1, "value": 1}):
    print(x)

