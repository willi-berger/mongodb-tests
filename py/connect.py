import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')

db = client.mytestdb


print(db.list_collection_names())
people = db.people

for person in people.find():
    pprint.pprint(person)
    print(person['firstname'])
