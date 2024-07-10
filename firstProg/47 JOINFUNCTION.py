
lis=["Code with Harry","The catalyst group","Pushkar raj thakur","Stock advisor","Corey schafer"]

for item in lis:
    print(item,"and",end=" ") # this a way to seperate list item with and without use of join function
print("Some other is still my favourite Youtube channel")

a=" and ".join(lis) # this join function works that they seperate list item with in this case seperate by (end)
print(a,"and Some other is still my favourite Youtube channel")