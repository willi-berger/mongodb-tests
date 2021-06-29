import pymongo
import datetime
from pymongo import MongoClient
 
client = MongoClient('mongodb://127.0.0.1:27017')


db = client.mytestdb

post = {"author": "Willi",
        "text": "My first blog post!",
        "tags": ["php"],
        "date": datetime.datetime.utcnow()}

db.posts.insert_one(post)