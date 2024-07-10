import random

"""random_number=random.randint(0,9)#they give any number between 1 to 9 
                            # in many time we run the code we'll get different values b/w them
print(random_number)
"""


"""print(random.random()) # give random number between 0 & 1 in decimal
print(random.random()*25)# give random number between 0 & 25 with decimal
"""

"""
d1=["Harry","Prince","Ganesh "]
print(random.choice(d1)) # thet give any list item in the list items
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

