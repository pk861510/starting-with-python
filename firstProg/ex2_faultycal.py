# design a calculator which will correcrly solve all the problems except the following ones
""" 45*3=555, 56+9 = 77,56/6=4
 Your program should take operator and the two numbers as input from the user
   and then return the result """

op=input("enter the operator which is use for you : ")
num1 = input("enter first number :")
num2 = input("enter second number :")

if (op=="*"):
   if int(num1)*int(num2)==45*3:
      print( 555 )
   else:
      print(int(num1)*int(num2))
elif(op == "+"):
   if(int(num1)+int(num2)==56+9):
      print(77)
   else:
      print(int(num1)+int(num2))
elif(op == "/"):
   if(int(num1)/int(num2)==56/6):
      print(4)
   else:
      print(int(num1)/int(num2))

else:
   print("you press invalid option")

