class Dad():
    basketball = 1
    dance = 5

class Son(Dad):
    # dance = 1
    basketball = 4
    def isdance(self):
        return f"yes i dance {self.dance} no of times"

class Grandson(Son):
    dance = 6 # this is not then find in son class if not in son then in dad class
    def isdance(self):
        return f"\n junction yeah !! "\
              f"yes i dance vert awesomely {self.dance} no of times"  # \ is used bcz new line not apere print in one line otherwise error is generated
    pass
siyaram = Dad()
sanjay = Son()
ashish = Grandson()

print(ashish.isdance())
print(ashish.basketball)
# print(ashish.guitaar)  # THIS GIVE ERROR BECAUSE THE  guitaar IS NOT FOUND IN ANT OF THE CLASSES SO ERROR IS GENERATED

# if we commont the isdance method of Grandson class then the isdannce method of class son use & variable dance is of Grandson used