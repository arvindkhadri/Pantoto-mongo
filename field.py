from panobj import PanObj
import storedata
class Field(PanObj):

    def __init__(self, sessionuser, deco, label, val = None):
        PanObj.__init__(self,sessionuser)
        self.decoration = deco
        self.label = label
        self.value = val
        self.id = "f" + str(self.getNextCounter())
        self.data = {"label":label, "decoration":deco, "_id": self.id, "value":self.value}
        storedata.save_data_into_db(self.data, self.__class__.__name__.lower())
   
    def getNextCounter(self):
        return storedata.incCounter(self.__class__.__name__.lower())
      

    def setvalue(self, val):
        self.value = val

    def getvalue(self):
        return self.value

    def getlabel(self):
        return self.label

    def getid(self):
        return self.id

    def getobj(self):
        return self
