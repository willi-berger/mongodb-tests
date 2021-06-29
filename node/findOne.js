var mongo = require('mongodb');

var MongoClient = mongo.MongoClient;
var url = 'mongodb://127.0.0.1/27017';

MongoClient.connect(url, function(err, db) {

    if (err) throw err

    var dbo = db.db('mytestdb')

    dbo.collection('people').findOne({}, function(err, result) {
        
        if (err) throw err;

        console.dir(result)
        db.close()
    })
    
}

);