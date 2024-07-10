
   # STATIC METHOD DO NOT TAKE ANY ARGUMENTS

class Employee():
    N0_of_leaves = 9
    no=0
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    no+=1

    def printdetails(self):
        return( f" Name of the Emplpyee is : {self.name}\n Salary of the Employee is :{self.salary} \n And Role is : {self.role}")

    @classmethod  # Class method access only class instance variable and we can access it through any instance or any instance variable or any calss
    def chamge_leaves(cls,newleaves):
        cls.N0_of_leaves=newleaves

    @classmethod
    def from_string(cls,str1):
        return cls(*str1.split("-"))  # Insted of writing following we can use *args in one line we complete the task

    @staticmethod
    def prnt(name):
        print("thats good prince "+ name)
        return "thenga"  # if we return something that is print if we can use this prnt staticmethod


harry=Employee('Harry',50000,'Instructor')
corey=Employee('Corey Schafer',60000,'Supervisor')

emp_3= Employee.from_string("Rohan-500000-Student")


print(corey.prnt("we proud of you")) # if we use print than only the return value printed
Employee.prnt("rhan") # in this case return value not printed because we do not use print statement
