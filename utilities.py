#!/usr/bin/python
# Filename: utilities.py
from datetime import date
import storedata

class History:

    # Every object has its history embedded in it.
    # TODO

    id_counter = 0 

    def __init__(self, pobj_id, modified_by, last_rev ):
        self.lastmodified = date.today()
        self.lastmodfiedby = ''
        self.panobjid = pobj_id 
        self.version = last_rev + 1 
        
        # Not sure how to increment version, 
        # will need to look up the last version each time
        self.__class__.id_counter += 1
        self.id = "h" + str(self.__class__.id_counter)
        # self.id is the id of the history object
        # panobjid = self.id+panobjid ; makes is a unique history object


    def __str__(self):
        printstr = "\nObject revision:" + self.version
        printstr += "\nLast Modified on:" + self.lastmodified.isoformat()
        printstr += "\nLast Modified by:" + self.lastmodifiedby
        printstr += "\nPanobj ID:" + self.panobjid
        printstr += "\nHistory Obj ID:" + self.id

    # These methods can be figured out once we 
    # understand persistence in this prototype
    
    def getprevious(self, pobj_id):
        pass

    def getnext(self, version):
        pass

    def getallhistory(self, pobj_id):
        pass


class User:
    
#    id_counter = 
    # get the latest counter for user, from the counter object in db
    # this object will be "u"+counter+1

    def __init__(self, fname, lname):
#        self.__class__.id_counter += 1 
        self.id = "u" + str(self.getNextCounter())
        self.firstname = fname
        self.lastname = lname
        data = dict({"firstname":fname,"lastname":lname,"_id":self.id})
        storedata.save_data_into_db(data, self.__class__.__name__.lower())
    def __str__(self):
        printstr = "\nUser details"
        printstr += "\nFirst name = " + self.firstname
        printstr += "\nLast name = " + self.lastname
        printstr += "\nRoles = " + self.roles

    def getuser(self):
        return user
        
    def getname(self):
        return self.firstname + " " + self.lastname

    def getid(self):
        return self.id

    def getNextCounter(self):
        return storedata.incCounter(self.__class__.__name__.lower())

class Group: # creating user groups

#    id_counter = 0

    def __init__(self, name):

        self.id = "g" + str(self.getNextCounter())
        self.groupname = name
        self.userlist =[]
        self.data = {"name":self.groupname,"_id":self.id, "list_of_users":self.userlist}
        storedata.save_data_into_db(self.data, self.__class__.__name__.lower())

    def getNextCounter(self):
        return storedata.incCounter(self.__class__.__name__.lower())

    def __str__(self):
        printstr = "\nUser details"
        printstr += "\nGroup name = " + self.firstname

    def getname(self):
        return self.groupname

    def getid(self):
        return self.id

    def getusers(self):
        return self.userlist

    def adduser(self,userid):
        self.userlist.append(userid)
        storedata.update_group(self.id, self.userlist, self.__class__.__name__.lower())
    
    def hasuser(self,userid):
        if userid in self.userlist:
            return True
        else:
            return False

class Role: #As a more intuitive alternative to Persona
    

    def __init__(self, rname, rdesc):
        self.id = "r" + str(self.getNextCounter())
        self.rolename = rname
        self.roledesc = rdesc
        self.userlist = []
        self.data = {"name":self.rolename,"_id":self.id, "list_of_users":self.userlist}
        storedata.save_data_into_db(self.data, self.__class__.__name__.lower())

    def getNextCounter(self):
        return storedata.incCounter(self.__class__.__name__.lower())

    def __str__(self):
        printstr = "\nRole details"
        printstr += "\nRole : " + self.rolename
        printstr += "\nDesc : " + self.roledesc

    def getid(self):
        return self.id

    def getusers(self):
        return self.userlist

    def adduser(self,userid):
        self.userlist.append(userid)
        storedata.update_group(self.rolename, self.userlist, self.__class__.__name__.lower())

    def hasuser(self,userid):
        if userid in self.userlist:
            return True
        else:
            return False

class Permissions:

    def __init__(self, dict=None):
        self.data = {}
        if dict is not None:
            sorted(self.data)
            self.data.update(dict)
    
    def convert_dict_values(self):        
        return self.data
        
    
    def __str__(self):
        print "\n" + str(self.data)


    def clear(self): 
        self.data.clear()
    
    def copy(self):
        if self.__class__ is Permissions:
            return Permissions(self.data)
        import copy
        return copy.copy(self)
    
    def keys(self): 
        return self.data.keys()
                        
    def items(self): 
        return self.data.items()
        
    def values(self): 
        return self.data.values()

    def getitem(self, key):
        print "Self data",self.data
        return self.data[key]

    def update(self,dict):
        return self.data.update(dict)
    
    def merge(self,dict):
        if len(self.data.keys()) == 0:
            self.data = dict
        else:
            for eachkey in self.data:
                if eachkey in dict.keys():
                    self.data[eachkey] = self.runrule(list(self.data[eachkey]),list(dict[eachkey]))
    def runrule(self,list1,list2):
		# rw U rw = rw
		# r- U -w = rw
		# rn U -w = rn
		# r- U nw = nw
		# -- U any = any (whatever permission prevails)
		# nn U any = nn (not visible)
		# Is a union more permissive and an intersection more restrictive?
		permstr = ""
		if len(list1) != len(list2):
			print "\nError in permissions definition"
			return "nn"
               # print "list1",list1
               # print "list2",list2
		for i in range(len(list1)):
			if list1[i] == 'n' or list2[i] == '-':
                		pass
                # do nothing to list 1
			elif list1[i] == '-' or list2[i] == 'n':
				list1[i]=list2[i]
			permstr += list1[i]
		
		return permstr



class Session:
    
    id_counter = 0

    def __init__(self, uid):
        self.__class__.id_counter += 1
        self.id = "s" + str(self.__class__.id_counter)
        self.userid = uid

    def __str__(self):
        printstr = "\nSession Details:" + self.id
        printstr = "\nUser:" + self.userid
        print printstr
