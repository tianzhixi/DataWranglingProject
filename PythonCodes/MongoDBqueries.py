# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:59:38 2015

@author: tyin
"""

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.examples
db.lincoln.insert(data)

# db.lincoln.remove()

db.lincoln.find().count()
db.lincoln.find({"type":"node"}).count()
db.lincoln.find({"type":"way"}).count()
len(db.lincoln.distinct("created.user"))

# Tope 5 users
result = db.lincoln.aggregate([{"$match":{"created.user":{"$exists":1}}}, 
                               {"$group":{"_id":"$created.user","count":{"$sum":1}}}, {"$sort":{"count":-1}}, {"$limit":5}])
for ele in result:
    pprint.pprint(ele)

# Numbers of users that contribute a particular times
result = db.lincoln.aggregate([{"$match":{"created.user":{"$exists":1}}}, 
                               {"$group":{"_id":"$created.user","count":{"$sum":1}}}, {"$group":{"_id":"$count","num_users":{"$sum":1}}}, {"$sort":{"_id":1}}])
for ele in result:
    pprint.pprint(ele)
    



# Top 5 amenities
result = db.lincoln.aggregate([{"$match":{"amenity":{"$exists":1}}}, 
                               {"$group":{"_id":"$amenity","count":{"$sum":1}}}, 
{"$sort":{"count":-1}}, 
{"$limit":5}])
for ele in result:
    pprint.pprint(ele)


# Top 5 religions
result = db.lincoln.aggregate([{"$match":{"amenity":{"$exists":1}, "amenity":"place_of_worship"}}, 
                               {"$group":{"_id":"$religion","count":{"$sum":1}}}, 
{"$sort":{"count":-1}}, 
{"$limit":5}])
for ele in result:
    pprint.pprint(ele)


# Top 5 denominations
result = db.lincoln.aggregate([{"$match":{"amenity":{"$exists":1}, "amenity":"place_of_worship"}}, 
                               {"$group":{"_id":"$denomination","count":{"$sum":1}}}, 
{"$sort":{"count":-1}}, 
{"$limit":5}])
for ele in result:
    pprint.pprint(ele)


# Top 5 cuisines in restaurants
result = db.lincoln.aggregate([{"$match":{"amenity":{"$exists":1}, "amenity":"restaurant"}}, 
                               {"$group":{"_id":"$cuisine","count":{"$sum":1}}}, 
{"$sort":{"count":-1}}, 
{"$limit":5}])
for ele in result:
    pprint.pprint(ele)

# Top 5 cuisines in fast foods
result = db.lincoln.aggregate([{"$match":{"amenity":{"$exists":1}, "amenity":"fast_food"}}, 
                               {"$group":{"_id":"$cuisine","count":{"$sum":1}}}, 
{"$sort":{"count":-1}}, 
{"$limit":5}])
for ele in result:
    pprint.pprint(ele)