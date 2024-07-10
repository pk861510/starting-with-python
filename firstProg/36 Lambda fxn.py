# Lambda function or anonymous function
"""def minus(x,y):
    return x-y

# minus = lambda x,y: x-y

print(minus(9,5))
"""
def a_first(a):
    return a[1]
a=[[1,14],[5,6],[8,23]]

a.sort(key=a_first) # key=lambdae
print(a)