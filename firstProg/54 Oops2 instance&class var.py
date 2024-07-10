class Employee(): # This is a class of Employee
    N0_of_leaves = 9
    pass

harry=Employee()  #in this way we cerate harry & corey two (instances)
corey=Employee()

harry.name  = 'Harry'  # These are (instance variables) of harry & corey
harry.salary = 50000
harry.role  = 'Instructor'

corey.name  = 'Corey Schafer'
corey.salary = 60000
corey.role  = 'Supervisor'

print(harry.salary)
print(harry.N0_of_leaves)  # instance variables access the class variable but do not change class variable by instance variable

print(harry.__dict__)
harry.N0_of_leaves=6 # This cereate a instance variable in harry name as harry.No_of_leaves and we do not change class variable using instance variable
print(harry.__dict__)

Employee.N0_of_leaves=5  # we can change class veriable using this method
print(Employee.N0_of_leaves)
print(harry.N0_of_leaves)
