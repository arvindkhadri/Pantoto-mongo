from pymongo import Connection
from utilities import *
#from exception import SessionFailed
i = -1
db_connection = Connection('localhost', 27017)
data_base = db_connection['prototypedb'] #The function is not needed, these two steps are needed always.
  
def save_data_into_db(data, model):
    collection = data_base[model]
# if model == "user" and  collection.find_one({'username':data['username']}): 
#	print "The user already exists."
#    else:
    return collection.insert(data)
    print "Successfully created ",model

def update_group(grp_name, data, model):
    collection = data_base[model]
    collection.update({"name":grp_name},{"$set":{'list_of_users':data}})

def check(username, passwrd):
    collection = data_base['user']
    try:
        if collection.find_one({'username':username})['username'] == username and collection.find_one({'username':username})['password'] == passwrd:
            return 1
    except TypeError:
        print 'Username doesnt exist'
        raise SessionFailed()
    else:
        raise SessionFailed()

def update(uname,data, model):
    collection = data_base[model]
    collection.update({'username':uname},{"$set":data})
    print collection.find_one({'username':data['username']})

def remove(name, model):
    collection = data_base[model]
    collection.remove({"username":name})

def list(model):
    collection = data_base[model]
    for x in collection.find():
        print  x['firstname']

def update_pagelet(data, model):
    collection = data_base[model]
    collection.update({'pagelet_name': data}, {"$set": {'status': "published"}})

def fetch_field(name):
    collection = data_base['field']
    return collection.find_one({'id':name})['label']
    
def fetch_ids(name):
    collection = data_base['group']
    ul = []
    ul = collection.find_one({'id':name})['list_of_users']
    return ul

def update_field(sessionuser, ans, pg_id):
    collection = data_base['pagelet']
    collection.update({'_id': pg_id}, {"$set": {'field_set':ans}})
   
def field_value(sessionuser):
    collection = data_base['pagelet']
    for f in collection.find():
        if sessionuser in f['authors']:
            return f['field_set']

def fetch_field_value(label, pagelet_id):
    collection = data_base['pagelet']
    x = collection.find_one({'_id':pagelet_id})['field_set']
    for i in x:
        if label in i:
            return i[label]
        else:
            pass

def update_pagelet_viewcategory(pagelet_id,view_id):
    collection = data_base['pagelet']
    collection.update({'_id':pagelet_id},{"$set":{'views':view_id}})

def getCounter(model):
    # counter {_id:0, user : num, pagelet : num,..}
    collection = data_base['counter']
    try :
        return collection.find_one({"_id":0})[model]
    except TypeError:
        collection.insert({"_id":0,model:0})
        return 0

def incCounter(model):
    collection = data_base['counter']
    try :
        c = collection.find_one({"_id":0})[model]
        collection.update({"_id":0},{"$set":{model:c+1}})
        return c+1
    except TypeError:
        collection.insert({"_id":0,model:1})
        return 1
