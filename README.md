# Mongo DB tests

## Start mongo server

Create a docker network (optional)


docker network create -d bridge docker-bridge-network

```
$ docker run --name mytest-mongo -d mongo:latest
```
listens on the standard MongoDB port *27017*.
Connect to a docker network with
```
docker network connect docker-bridge-network mytest-mongo
```


 ## Connect to DB

 ```
$ docker run -it --network docker-bridge-network --rm mongo mongo --host mytest-mongo
 ```


## General Usage
Start mongo client from command line
```
$ mongo
```

```
MongoDB shell version v3.6.8
connecting to: mongodb://127.0.0.1:27017
Implicit session: session { "id" : UUID("4c0ad58e-9382-486f-a337-eb85cbc48460") }
MongoDB server version: 4.4.6
```

* show dbs
* use mytestdb
* show collections

### Selcet & Find Examples

* db.people.find({"city": /St..Veit/});
```
{ "_id" : ObjectId("60bb48af0ebe2171ced6d30f"), "firstname" : "Willi", "lastname" : "Berger", "birthdate" : "1968-05-05", "city" : "St. Veit" }
```

* db.people.count({"city": /St..Veit/});

### Import Json file

$ mongoimport --db=mytestdb --collection=zips  zips.json



### Aggregation
```
db.zips.aggregate( [
   { $group: { _id: "$state", totalPop: { $sum: "$pop" } } },
   { $match: { totalPop: { $gte: 10*1000*1000 } } }
] )
```


## Python client

Install with pip
```
$ python -m pip install pymongo
```
