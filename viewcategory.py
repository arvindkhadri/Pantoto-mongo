from panobj import PanObj
import cPickle
import storedata

class ViewCategory(PanObj):

    def __init__(self,sessionuser,vcname,perm_id, perm, persona):
        PanObj.__init__(self,sessionuser)
        self.name = vcname
        self.permissions_id = perm_id
        self.permissions = perm
        self.workflowrole = persona # View is associated with a role
        self.id = "vc" + str(self.name)
        self.data = {"id":self.id,"name":self.name, "permissions": self.permissions_id}
        storedata.save_data_into_db(self.data, self.__class__.__name__.lower())

    def convert_dict_values(self):        
        return dict(self.permissions)
   
    def edit(self,perm):
        pass

    def delete():
        pass

    def acl(self,sessionuserid):
        # need not check workflowuser
        if self.workflowrole.hasuser(sessionuserid):
            grpid = ''
            for gid in self.permissions.keys():
                grp_users = storedata.fetch_ids(gid)
                #grp = cPickle.load(open(gid+".obj",'rb'))
                if sessionuserid in grp_users:
                    grpid = gid
                    break
            return self.permissions.getitem(grpid) # Returns a field access set
        else:
            return Null

    def getid(self):
        return self.id
