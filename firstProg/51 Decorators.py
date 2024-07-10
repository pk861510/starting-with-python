"""
def function1():
    print("Makes life easy stay Healthy")

func1 = function1
del function1
func1()
"""
"""
def function2(num):
    if num==0:
        return print
    if num==1:
        return int
val=function2(int(input("input 1 or 0: ")))
print(val)
"""
"""
def function3(func):
    func("This is working")

function3(print)
"""
def funcret(func1):
    def now_execute():
        print("Executing the decorator")
        func1()
        print("Executed the dexorator func1")
    return now_execute

@funcret # This type of decorators used before function name
def who_is_Prince():
    print("Prince become self made")

# who_is_Prince=funcret(who_is_Prince) # We can wrier shortly this line @funcret before function
who_is_Prince()
