from ctypes import *

msvcrt = cdll.msvcrt
message_string = "hellow world!\n"

msvcrt.wprintf("Testing: %s", message_string)

str_p = c_wchar_p("hello world.")

#struct
class beer_recipe(Structure):
    _fields_ = [
                ("amt_barley", c_int),
                ("amt_water", c_int),
                ]
    
a = 10
b = 20

my_beer = beer_recipe(a, b)
print(my_beer.amt_barley, my_beer.amt_water)

