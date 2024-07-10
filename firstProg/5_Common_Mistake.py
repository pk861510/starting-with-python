import time
from datetime import datetime

def display_time(time = datetime.now()) :  #This will give same time without chang in second
    print(time.strftime("%b %d %Y, %H:%M:%S"))


def display_time(time =None) :  #This will give same time with chang in second
    if time== None:
        time =  datetime.now()

    print(time.strftime("%b %d %Y, %H:%M:%S"))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()


