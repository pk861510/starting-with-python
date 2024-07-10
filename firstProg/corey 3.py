class Employee:

    raise_amount= 1.09
    no_of_employees = 0

    def __init__(self,first,last,pay):   # __init__ is a method they receive inatances(self) as the first arguments we give any name to instance
        self.first=first       #they work same (empl_1.first = 'Prince')
        self.last=last
        self.pay=pay
        self.email=(first+ '.' + last+'@company.com')

        Employee.no_of_employees += 1  # We should acces the class variable through the class
    def fullname(self):
            return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        # self.pay=int(self.pay*1.04)
        self.pay=int(self.pay * self.raise_amount) #  or we can use Employee.raise amount

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,str1):
        first, last, pay = str1.split("-")
        return cls(first,last,pay)
        # return cls(*str1.split("-"))

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True



print(Employee.no_of_employees)
empl_1 = Employee('Prince','Sah',50000)
empl_2 = Employee('Corey','Schafer',60000)
# empl_3 = Employee('Corey','Schafer',60000) # if we uncomment this line and run tne code than we get no of employee is 3
print(Employee.no_of_employees)

new_str1 = "Kundan-Singh-70000"
# first = new_str1.split("-")
# new_emp1 = Employee(first[0],first[1],first[2])
# print(new_emp1.fullname())
new_emp1 = Employee.from_string(new_str1)
print(new_emp1.email)

import datetime
my_date = datetime.date(2023,4,2)
print(Employee.is_workday(my_date))
