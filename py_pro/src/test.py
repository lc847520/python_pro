import os
import sys
import math
from builtins import isinstance
from abc import ABCMeta, abstractmethod, abstractproperty

class ProtectAndHidex(object):
    def __init__(self, x):
        assert isinstance(x, int), "x must be an integer."
        
        self.__x = ~x
        
    def get_x(self):
        return ~self.__x
    
    def set_x(self, x):
        assert isinstance(x, int), "x must be an integer."
        
        self.__x = ~x
    
    #x = property(get_x, set_x)
    
    @property
    def x(self):
        def fget(self, x):
            return ~self.__x
        
        def fset(self, x):
            assert isinstance(x,int), "x must be an integer."
            self.__x = ~x
            
        return locals()

class Circlet(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2
    
    @property
    def perimeter(self):
        return 2*math.pi * self.radius

def my_func():
        
    for i in range(10):
        print(i)


class Foo:
    __metaclass__ = ABCMeta
    @abstractmethod
    def spam(self):
        pass
    
    @abstractproperty
    def name(self):
        pass
class Grok(object):
    def spam(self):
        print("Grok.spam")

if __name__ == "__main__":
    print ("main starting......")
    
    my_func()
    
    c = Circlet(4)
    
    print( c.area)
    
    Foo.register(Grok)
    
    Foo.spam()
    
    
    
    
    
    
    
