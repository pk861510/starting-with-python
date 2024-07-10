list1=["prince","aniket","rahul","sanjeev","the legend"]
"""
  i=1
for item in list1:
    if i%2==0:
        print(item)
    i+=1
"""
"""
i=1
for item in list1:
    if i%2 is not 0:
        print(f"the selected name {item}")
    i+=1
"""
"""
i=1
for item in list1:
    if i%2 is 0:
        print(f"the selected name {item}")
    i+=1
"""

for index,item in enumerate(list1):
    if index %2==0:
        print(f"the selected name {item}")  #this is enumerate fumction work

























