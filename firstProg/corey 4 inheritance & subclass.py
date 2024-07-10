
class Employee:

    raise_amount= 1.04
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

class Developer(Employee):
    raise_amount= 1.09 # When this line is umcommented then emp_1.apply raise is increse by 1.09 because of Developer class. ( firstly search in Developer and than Employee)

    def __init__(self,first,last,pay,prog_len):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_len

class Mannager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->>",emp.fullname())




dev_1 = Developer('Prince','Sah',50000, "Python")          # if we use Employee insted of Developer  then (print(empl_1.email) do no affected because DEveloper access all the Employee class
dev_2 = Developer('Corey','Schafer',60000 , "Java")
# l=[dev_2,dev_1]
mgr_1 = Mannager("Modassir","Alam", 62000 , [dev_1])  # also we can pass list of developer in this manager class by using *args

print(isinstance(mgr_1,Mannager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))
print(issubclass(Developer,Employee))
print(issubclass(Mannager,Employee))
print(issubclass(Mannager,Developer))






# print(dev_1.email)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emp()



