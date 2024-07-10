p = open("prince.txt","rt")
print(p.readlines())
# print(p.readline())
# print(p.readline())
# print(p.readline())

"""content = p.read()
for line in content:
    print(line,end="")"""
p.close()

"""p = open("prince.txt","rt")
content = p.read(56546)
print("1" ,content)

content = p.read(9)
print("2",content)
p.close()"""