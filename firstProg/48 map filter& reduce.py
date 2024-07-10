list1= ["5","8","9","7"]
"""
# number=list1[2]+2 # if we execute this line we can typecast list1 from string to integer
for i in range(len(list1)):
    # without use of map fumction typecast list1 from string to integer
    list1[i]=int(list1[i])
number=list1[2]+2
print(number)
"""
# .......................use of map fuction...............................

"""list1=list(map(lambda x:int(x),list1)) # all string typecast into integer
number=list1[2]+2
print(number)


list2=list(map(lambda y:y*y,list1)) # all typecasted list1 apply on square function
print(list2)
"""
"""
def square(x):
    return x*x
num=[1,2,3,4,5,6,7,8,9]
square1=list(map(square,num))
print(square1)
"""
# num=[1,2,3,4,5,6,7,8,9]
# square1=list(map(lambda x:x*x,num))
# print(square1)

# def square(x):
#     return x*x
# def cube(x):
#     return x*x*x
# func=[square,cube]
# for i in range (5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

# .......................use of filter fuction...............................

# list_1=[1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5
# print(is_greater_5(7)) #this return true or false
#
# number1=list(filter(is_greater_5,list_1))
# print(number1)


# .......................use of reduce fuction...............................
from functools import reduce
list_2=[1,2,3,4,5,6,7,8,9]
# sum=0
# for item in list_2:
#     sum=sum+item
# print(sum)
#
# sum=reduce(lambda x,y:x+y,list_2)
# print(sum)

# import time
# print(time.asctime())