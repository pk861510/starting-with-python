"""f= open("prince.txt")
print(f.tell())# tell is use to find the file pointer exctly present in which position
print(f.readline(),end=" ")# after print first line the pointer goes to second line then we use f.tell() pointer gives desire position of pointer
print(f.tell())
print(f.readline(),end=" ")
f.close()"""

f= open("prince.txt")
print(f.tell())
print(f.readline(),end=" ")
f.seek(0)# if i use seek 0 then file pointer goes to 0 and again i print new line then print with starting
print(f.readline(),end=" ")
f.seek(36)#file pointer goes to 36th position
print(f.readline(),end=" ")
f.close()