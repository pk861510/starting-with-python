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

    @classmethod
    def from_string(cls,str1):
        return cls(*str1.split("-"))  # Insted of writing following we can use *args in one line we complete the task

    @staticmethod
    def prnt(name):
        print("thats good prince "+ name)
        return "thenga"  # if we return something that is print if we can use this prnt staticmethod

class Programmer(Employee):
    def __init__ (self,name,salary,role,language):
        # self.name= name
        # self.salary= salary
        # self.role = role

        # super.__init__()
        super().__init__(name,salary,role)
        self.language = language

        def print_details():
            print(f"Name of the Employee is {self.name},Role is { self.role}& salary is {self.salary}")


harry=Employee('Harry',50000,'Instructor')
corey=Employee('Corey Schafer',60000,'Supervisor')
prince = Programmer("Prince",700000,"Programmer","python")

print(prince.language,prince.role)
print(prince.printdetails())
