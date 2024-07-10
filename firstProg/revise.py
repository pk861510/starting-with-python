"""# import pandas
import random
print("love yourself")"""
"""print("hello\n")#\n is use to a new line
print("\tfocus on your career",end="")#end= is use to add new line in any line which already ecsist
print("Love yourself")"""

"""n1=input("Enter first number: ") #7
n2=input("Enter second number: ")
print("Sum of these two number is",int(n1)+int(n2))"""
"""var1="Hello prince"
var2=" you are on right dirtection or not"
print(var1+var2)"""
"""
var1="4"
var2=" you are on right dirtection or not"
print(var1+var2)"""

mystr="focus on whatever you do for yourself"
mystr1="focusonwhateveryoudoforyourself"
"""print(mystr[0:5])
print(len(mystr))
print(mystr[-8:])
print(mystr[29:37])"""

"""print((mystr[::-1]))# if we put spacing character value -ve than the whole string print in reverse order

print(mystr.isalnum())#not alphanumeric bcz space between two character is present
print(mystr1.isalnum())# alphanumeric bcz space between two character is not present
     #false and true are bullion character
print(mystr.isalpha())
print(mystr.endswith("yourself"))
print(mystr.count("o"))
print(mystr.capitalize())# first latter capitalize
print(mystr.find("you"))"""


"""with open("prince.txt") as f:
    # a = f.read()
    a=f.readlines()
    print(a)
"""
f=open("prince.txt","rt")
a=f.read()
print(a)

a= int(input("Enter a number want to print their table : "))
i=1
while(i<=10):
    print( a,"*" , i , "=" ,a*i)
    i = i + 1


mystr="Hell"
my_num = 10
if(isinstance(mystr,str) and mystr == "Hello"):
    print("mystr is an string %s" %mystr)
    