class Student():
    pass

harry = Student
corey = Student

# print(harry)
# print(corey)

harry.name="Harry"
harry.std=12
harry.subject=["physics","chemistry","biology"]

corey.name="Corey"
corey.std= 'B.tech'
corey.subject=["EG&D","PPS","Mechanics"]

print(corey.name,corey.subject)
print(harry.__dict__)
