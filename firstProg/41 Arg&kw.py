"""def func1(a,b,c,d):
    print(a, b, c, d)
    print(type(e))

func1("prince","Rahul","Dhiraj","Sonu",8)# if we pass an extra arguments then we'll make extra function call
                                         #that is not conventional so we use args and kwargs
   """

"""def func2(*args):
    print(type(args))#type of args is touple if we pass list or touple 
    print("The selected student is : ")
    for item in args:
        print (item)

lis=["prince","Rahul","Dhiraj","Sonu","and some other"]#if we make an extra arguments than we do not need to create an extra function call
func2(*lis)
"""
# def func2(pri,*args):
#     """ NOTE: if we change the position to normar variable and args then the error is ganerated because the convensional way is that
#       firstly we use normal arguments than *args than **kwargs"""
#     print(f"\nthe normal variable: {pri}")# This is normal variable
#     print("The selected student is : ")
#     for item in args:
#         print (item)
#
# normal_var=8
# lis=["prince","Rahul","Dhiraj","Sonu","and some other"]#if we make an extra arguments than we do not need to create an extra function call
# func2(normal_var,*lis)
# print(func2.__doc__)

"""
def func2(pri,*argspri,**kwargs):# if we make **kwargs and we'll not pass any arguments than no error ganerated
         #we'll free to write any name after *args and **kwargs for example *argsprince and **kwargsprince

    print(f"{pri}")# This is normal variable
    for item in argspri:
        print (item)

    for key,value in kwargs.items():
            print(f"{key} is {value}")


normal_var= "i am normal arguments and the selected students are :"
lis=["prince","Rahul","Dhiraj","Sonu","and some other"]
dic1={"prince":"the programmer ","harry":"youtuber","AS pandit ":"My favourite persion"}

func2(normal_var,*lis,**dic1)
"""


def func2(pri, *argspri, **kwargs):
    print(f"{pri}")  # This is normal variable
    for item in argspri:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is {value}")

normal_var = "i am normal arguments and the selected students are :"
lis = ["prince", "Rahul", "Dhiraj", "Sonu", "and some other"]
dic1 = {"prince": "the programmer ", "harry": "youtuber", "AS pandit ": "My favourite persion"}

func2(normal_var, *lis, **dic1)

def funargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} is a {value}")

kwa = {"Prince":"The programmer ", "Shivam ": "Student","Harry ":"The youtuber"}
funargs(**kwa)