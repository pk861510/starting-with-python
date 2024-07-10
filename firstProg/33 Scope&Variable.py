"""l=10
def glob ():
    a=5
    l=9
    print(a+l)
glob()
print(l)
# print(a)
             #o/p=14&10
"""
"""
l=10#giobal vaariable
def glob ():
    a=5 #local variable
    # l=9# local
    print(a+l)
glob()
print(l)
                 #o/p=15&10
# print(a)# name error because a is defined in function not in globally
"""
"""l=10#giobal vaariable

def glob ():
    a=5 #local variable
    global l #  global l give permission to chang global variable or assign values to it
    l=9# local
    print(a+l)
glob()
print(l)"""

x=55
def prince():
    x=20
    def rohan ():
        global x
        x=60
        # print(x) #print 60 because we halve us to global and this print serch x in globly bce local var x  f,]\ gtbe x
        #
        #
        #
        #
        #
        #
        #
        # ,l;;;;;;;;;'inot created in rohab function
    print("Before calling rohan x is :", x)
    rohan()
    print("After calling rohan x is :", x)
prince()
print(x)