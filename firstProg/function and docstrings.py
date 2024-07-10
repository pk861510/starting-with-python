"""
a=9
b=8
print(sum((a,b)))"""
def function1(a,b):
    """this funstion works only two number this
                not works more than two number """
    
    average = (a+b)/2
    print(average)
    return average
print(function1.__doc__)

v=function1(6,8)

print(v)