from pymongo import Connection

connection = Connection('localhost',27017)
db = connection['prototypedb']
collection = db['counter']
data = {'_id':0,'user':0,'group':0,'pagelet':0,'viewcategory':0,'role':0,'field':0}
collection.insert(data)
