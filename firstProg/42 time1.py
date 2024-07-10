import time

"""
initial = time.time()#this give exect time of here
# print (initial)#ye milisecond ki bhi accuracy rakhti hai
k=0
while(k<4):
    print("Starting of the day with this code")
    # time.sleep(2)
    k+=1
final1=time.time() - initial
print(f"\t\t\t\t\t\t\twhile loop run in {final1} seconds")

initial2= time.time()
for i in range(4):
    print("Starting of the day with this code")
    # time.sleep(2)
final2=time.time() - initial2
print(f"\t\t\t\t\t\t\tfor loop run in {final2} seconds")
print(f"Execution time of while loop{final1} & for loop {final2}")
"""
local_time = time.asctime(time.localtime(time.time()))# This give exact local time
print(local_time)
print(time.asctime())

for i in range (5):
    print("print all code gap of 2 second bcz we use time.sleep(2)")
    time.sleep(1)#we can sleep any where gap of program







