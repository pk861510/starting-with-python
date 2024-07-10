# how to imports works in python
import sys
print(sys.path) #these give all the path details where's module or something is imported in the program
                #thats the region we do not make python file as a module name
import file2
# print(a) #this give error bcz we do not a variable in file1 acces from file2 then use print(file2.a)
print(file2.a)
print(file2.joke())

# a=file2.joke()
# print(a)

