"""
Once you download and install MongoDB (install with all the default options)
Go to command prompt (or terminal)
and type the command: net start MongoDB
there should be a message that says the database started successfully and you're good to go


https://www.w3schools.com/python/python_mongodb_insert.asp is a link that has everything you need to know


After you are done with the database run the command in terminal: net stop MongoDB


IF YOU RUN THIS SCRIPT OVER AND OVER AGAIN YOU WILL BE REPEATEDLY ADDING IN THE SAME DOCUMENTS
"""

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
artciles = mydb["info"]

mydict = { "url": "example", "tags": ["red", "blue", "green"] }
mydict2 = { "url": "example2", "tags": ["blue", "green"] }
mydict3 = { "url": "example3", "tags": ["red", "blue"] }
"""
out dictonary format is probably going to be a diction with url and tag and keys and a string and array of strings respectively
"""


artciles.insert_one(mydict)
artciles.insert_one(mydict2)
artciles.insert_one(mydict3)


"""
to find all articles which have a particular tag - THIS doesn't work yet 

mydoc = mydb.articles.find({"tags": { "$elemMatch": { "$eq": "red" } }})

for x in mydoc:
  print(x)

"""



