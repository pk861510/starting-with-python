class Employee:

    raise_amount= 1.09

    def __init__(self,first,last,pay):   # __init__ is a method they receive inatances(self) as the first arguments we give any name to instance
        self.first=first       #they work same (empl_1.first = 'Prince')
        self.last=last
        self.pay=pay
        self.email=(first+ '.' + last+'@company.com')

    def fullname(self):
            return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        # self.pay=int(self.pay*1.04)
        self.pay = int(self.pay * self.raise_amount) #  or we can use Employee.raise amount



empl_1 = Employee('Prince','Sah',50000)
empl_2 = Employee('Corey','Schafer',60000)

print(empl_2.fullname())

print(empl_1.pay)
empl_1.apply_raise()
print(empl_1.pay)

empl_1.raise_amount=1.7 # the
print(Employee.raise_amount)
print(empl_1.raise_amount)
print(empl_2.raise_amount)

# print(empl_1.__dict__)
# print(empl_2.__dict__)
# print(Employee.__dict__)



"""
"""