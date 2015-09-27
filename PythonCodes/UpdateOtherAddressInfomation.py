# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:09:31 2015

@author: tyin
"""

result = db.lincoln.aggregate([{"$match":{"address.country":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.country","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)


result = db.lincoln.aggregate([{"$match":{"address.state":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.state","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)


result = db.lincoln.aggregate([{"$match":{"address.city":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.city","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)

# There are three "Lincoln, NE"s, although find_one can let me change one by one, I still 
# checked after each change to make sure I change everyone of them.
city = db.lincoln.find_one({"address.city":"Lincoln, NE"})
pprint.pprint(city)
cityupdate = db.lincoln.update({"address.city":"Lincoln, NE"}, 
                               {"$set":{"address.city":"Lincoln", "address.state":"NE"}})
city = db.lincoln.find_one({"address.housename":"New Covenant Community Church"})
pprint.pprint(city)


city = db.lincoln.find_one({"address.city":"Lincoln, NE"})
pprint.pprint(city)
cityupdate = db.lincoln.update({"address.city":"Lincoln, NE"}, 
                               {"$set":{"address.city":"Lincoln", "address.state":"NE"}})
city = db.lincoln.find_one({"address.housenumber":"5200 Suite 1"})
pprint.pprint(city)


city = db.lincoln.find_one({"address.city":"Lincoln, NE"})
pprint.pprint(city)
cityupdate = db.lincoln.update({"address.city":"Lincoln, NE"}, 
                               {"$set":{"address.city":"Lincoln", "address.state":"NE"}})
city = db.lincoln.find_one({"address.housename":"The Courtyards"})
pprint.pprint(city)


# postcode
result = db.lincoln.aggregate([{"$match":{"address.postcode":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.postcode","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)

# only one problematic entry
postcode = db.lincoln.find_one({"address.postcode":"NE 68339"})
pprint.pprint(postcode)
postcodeupdate = db.lincoln.update({"address.postcode":"NE 68339"},
                                   {"$set":{"address.postcode":"68339", "address.state":"NE"}})
    

# housename
result = db.lincoln.aggregate([{"$match":{"address.housename":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.housename","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)

# I don't think it's necessary to change this one
housename = db.lincoln.find_one({"address.housename":"Suite #204"})
pprint.pprint(housename)


# the followings are all OK
result = db.lincoln.aggregate([{"$match":{"address.housenumber":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.housenumber","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)


result = db.lincoln.aggregate([{"$match":{"address.suite":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.suite","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)
    
    
result = db.lincoln.aggregate([{"$match":{"address.unit":{"$exists":1}}}, 
                               {"$group":{"_id":"$address.unit","count":{"$sum":1}}}, {"$sort":{"count":-1}}])
for ele in result:
    pprint.pprint(ele)