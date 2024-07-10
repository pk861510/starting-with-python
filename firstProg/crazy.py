"""from turtle import *
color("red")
begin_fill()
pensize(5
        )
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
"""


import time

def fun(*args):
    l1 = len(args)
    for i in range(l1):
        print(f" {args[i]}")
        time.sleep(3)
d1=["Hiii","How are you  ","today i told you something","whatever in my mind","you are the happiest person in the world ","you "
        " you deserve batter than expacted ","do not waste time for thinking of others ","do not fall in love with  whom who not show intrest in you "
            "be the best version of yourself","do not waste 1% of your time fow who do not deserve","Love Yourself","Respect the parents",
    "keep growing ","Welcome failure ","welcome Embarrasment","they give you chance to correct Yourself","Thank you","Keep Smiling"]
fun(*d1)


"""
import math
from turtle import*
def hearta(k):
    return 15 * math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3 * k)-\
            math.cos(4*k)


speed(0)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb((i)*20))
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()
"""

























