class Employee:
    # pass  # pass only given when we do not initialize any method within a class
    def __init__(self,first,last,pay):   # __init__ is a method they receive inatances(self) as the first arguments we give any name to instance
        self.first=first       #they work same (empl_1.first = 'Prince')
        self.last=last
        self.pay=pay
        self.email=(first+ '.' + last+'@company.com')

    def fullname(self):
            return "{} {}".format(self.first,self.last)


empl_1 = Employee('Prince','Sah',50000)
empl_2 = Employee('Corey','Schafer',60000)

print(empl_2.fullname())

# print(empl_1)
# print(empl_2)

"""
# insted of assigning these value seperately we can create a function in class then we can remove pass


empl_1.first = 'Prince'
empl_1.last = 'Sah'
empl_1.email = 'Prince.Sah@company.com'
empl_1.pay = 50000

empl_2.first = 'Corey'
empl_2.last = 'Schafer'
empl_2.email = 'Corey.Schafer@company.com'
empl_2.pay = 60000
"""
# print(" Full name of Employee : {} {} ".format(empl_1.first,empl_1.last)) # instef of writing thesr we can create function in under class

print(empl_1.email)
print(empl_2.email)


