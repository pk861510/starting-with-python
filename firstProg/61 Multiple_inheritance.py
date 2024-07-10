class Employee():
    N0_of_leaves = 9
    # var = 7
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):
        print( f" Name of the Emplpyee is : {self.name}\n Salary of the Employee is :{self.salary} \n And Role is : {self.role}\n")

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

class Player():
    no_of_game = 6
    var= 8
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        print(f"\nName is {self.name} and game is {self.game}\n")

class Cool_programmer(Employee,Player):  # If we try to access any variable or anything then firstly search in Employee class if not  than find in Player class
          # IF WE WANT FIRSTLY SEARCH ANTYHING IN PLAYER CLASS THEN WE CAN Cool_Programmer(Player , Employee) to create cool_programmer class
    # var = 9
    language = "C++"
    # def __init__(self,name,salary,role):
    #     super().__init__(name,salary,role)
    #     self.proglen = self.language
    def printlanguage(self):
        print(self.language)


harry=Employee('Harry',50000,'Instructor')
corey=Employee('Corey Schafer',60000,'Supervisor')

saurabh = Player("Saurabh Yadav",["Cricket"])
prince = Cool_programmer("Prince",70000,"Programmer")

saurabh.printdetails()
prince.printdetails()

print(prince.var) # If var of coolprogramer present then those value print then employee and then lastly find in player class
prince.printlanguage()