# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:05:42 2015

@author: tyin
"""
# Street names with only a capital letter
street = db.lincoln.find({"address.street":"K"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"K"}, 
                                 {"$set":{"address.street":"K Street"}})

street = db.lincoln.find({"address.street":"O"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"O"}, 
                                 {"$set":{"address.street":"O Street"}})

street = db.lincoln.find({"address.street":"P"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"P"}, 
                                 {"$set":{"address.street":"P Street"}})




# Other situations
street = db.lincoln.find({"address.street":"NW 1st St #102"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"NW 1st St #102"}, 
                                 {"$set":{"address.street":"Northwest 1st Street", "address.unit":"#102"}})

street = db.lincoln.find({"address.street":"South 10th"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"South 10th"}, 
                                 {"$set":{"address.street":"South 10th Street"}})

street = db.lincoln.find({"address.street":"Pioneer Woods Drive #110"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"Pioneer Woods Drive #110"}, 
                                 {"$set":{"address.street":"Pioneer Woods Drive", "address.unit":"#110"}})

street = db.lincoln.find({"address.street":"North 12th"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"North 12th"}, 
                                 {"$set":{"address.street":"North 12th Street"}})

street = db.lincoln.find({"address.street":"NW 1st"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"NW 1st"}, 
                                 {"$set":{"address.street":"Northwest 1st Street"}})

street = db.lincoln.find({"address.street":"North 8th Street, #214"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"North 8th Street, #214"}, 
                                 {"$set":{"address.street":"North 8th Street", "address.unit":"#214"}})


street = db.lincoln.find({"address.street":"Eagle Ridge Road #26"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"Eagle Ridge Road #26"}, 
                                 {"$set":{"address.street":"Eagle Ridge Road", "address.unit":"#26"}})

street = db.lincoln.find({"address.street":"NW 1st St #300"})
for ele in street:
    pprint.pprint(ele)
streetupdate = db.lincoln.update({"address.street":"NW 1st St #300"}, 
                                 {"$set":{"address.street":"Northwest 1st Street", "address.unit":"#300"}})