class Employee():
    N0_of_leaves = 9

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):
        return( f" Name of the Emplpyee is : {self.name}\n Salary of the Employee is :{self.salary} \n And Role is : {self.role}")


harry=Employee('Harry',50000,'Instructor')
corey=Employee('Corey Schafer',60000,'Supervisor')

"""
harry.name  = 'Harry'  # These are (instance variables) of harry & corey
harry.salary = 50000
harry.role  = 'Instructor'

corey.name  = 'Corey Schafer'
corey.salary = 60000
corey.role  = 'Supervisor'
"""

print(harry.salary)

print(harry.printdetails(),"\n")  # If we remove the parenthasis () then print this line we can see prints the method insted of  the return value
print(corey.printdetails())