
"""
           #Prince soln
a= int(input("Enter number of row you want to print : "))
b= bool( int( input("1 for true and 0 for false : ")))
def star(a,b):
    if b==True:
        c=1
        while c<=a:
            print(c*"*")
            c=c+1
    else:
        while a>0:
            print(a*"*")
            a=a-1

star(a,b)

"""
"""
     pattern printing
     input = integer n
     boolean = True or False
         true n=5
         *
         **
         ***
         ****
         *****
         false n=5
         *****
         ****
         ***
         **
         *
"""

"""row = int(input("Enter number of row you want to print: "))
boolion = bool(int(input("Enter boolion 0 for false and 1 for true: ")))
if( boolion==True):
    for i in range(1, row + 1):
        # print(i*"*")
        for j in range(1,i+1):# 1 insted of writing of these three line we can write only one line of code ie: print(i*"*")
            print("*",end="")# 2
        print()# 3
elif boolion==False:
    for i in range(row,0,-1):
        # print(i * "*") # try only these code
        for j in range(1,i+1):# 1 insted of writing of these three line we can write only one line of code ie: print(i*"*")
            print("*",end="")# 2
        print()# 3

"""









