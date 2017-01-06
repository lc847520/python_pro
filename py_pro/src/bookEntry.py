import os
import sys

class AddrBookEntry(object):
    
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        
        print("create instance for:", self.name)
        
    def updatePhone(self, newph):
        self.phone = newph
        print("update phone for:", self.name)
        
      
class EmpAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em
        
        print("EmpAddrBookEntry:__init__: email =" ,self.email, "empid=",self.empid)
    def updateEmail(self, newem):
        self.email = newem
        print("EmpAddrBookEntry:updateEmail: updateEmail =", self.email)

def fun_log(fn):
    def wrapper(*args, **kwargs):
        print ("Before Calling ", fn.__name__)
        retval = fn(*args, **kwargs)
        print ("After Calling %s" ,fn.__name__)
        return retval
    return wrapper


@fun_log    
def greeter(what="world"):
    print ("Has excuted!!")
    return ("Hello %s" ,what)
  
if __name__ == "__main__":
    
    print("main start")
    
    bookEntry = AddrBookEntry("liuchun", "1213412431")
     
    bookEntry.updatePhone("4523452345")
     
    empAddrEentry = EmpAddrBookEntry("liuchun", "123456789", 199, "xxx@aaa.com")
    
    print(greeter("You"))  
    
    print("main end......")
     
            
       
     
