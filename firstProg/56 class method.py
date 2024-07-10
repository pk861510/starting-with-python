
  # ..............................Classmethod...................................
class Employee():
    N0_of_leaves = 9

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):
        return( f" Name of the Emplpyee is : {self.name}\n Salary of the Employee is :{self.salary} \n And Role is : {self.role}")

    @classmethod  # Class method access only class instance variable and we can access it through any instance or any instance variable or any calss
    def chamge_leaves(cls,newleaves):
        cls.N0_of_leaves=newleaves


harry=Employee('Harry',50000,'Instructor')
corey=Employee('Corey Schafer',60000,'Supervisor')

harry.chamge_leaves(45)    # We can access the No_of_leaves of claa from instance as well as class.
# Employee.chamge_leaves(45)
print(Employee.N0_of_leaves)
print(harry.N0_of_leaves)


# Biggest benifit of class methos is that we can use it as an alternative constructor which will discuss in the next video








