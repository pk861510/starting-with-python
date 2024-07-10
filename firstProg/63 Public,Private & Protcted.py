# PUBLIC -
# PROTCTED -
# PRIVATE -

class Employee():
    N0_of_leaves = 9
    No_of_Emp = 0
    PUBLIC= 6
    _protcted = 8
    __private = 766

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        Employee.No_of_Emp = Employee.No_of_Emp + 1 # We can increment No_of_Emp by use of Empployee class because one in many time we create instances that time __init__ function call

    def printdetails(self):
        return( f" Name of the Emplpyee is : {self.name}\n Salary of the Employee is :{self.salary} \n And Role is : {self.role}")

    @classmethod  # Class method access only class instance variable and we can access it through any instance or any instance variable or any calss
    def chamge_leaves(cls,newleaves):
        cls.N0_of_leaves=newleaves

    @classmethod
    def from_string(cls,str1):
        return cls(*str1.split("-"))  # Insted of writing following we can use *args in one line we complete the task


harry=Employee('Harry',50000,'Instructor')
corey=Employee('Corey Schafer',60000,'Supervisor')
emp_3= Employee.from_string("Rohan-500000-Student")

print(harry.PUBLIC)
print(harry._protcted)
print(harry._Employee__private)  # we can access the protected variable only when the istancesname_Classname__protected variable name
# name mangling