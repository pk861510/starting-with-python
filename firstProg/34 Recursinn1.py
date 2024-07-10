"""def fact2(fact1):
    print("Prince",fact1)
fact2("is a good boy")
"""
"""
def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)

    return fact


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return (n*factorial_recursive(n-1))

print(factorial_recursive(int(input("Enter no for factorial from recursive method: "))))
print(factorial((int(input("Enter number you want to Factorial from ilterative method: ")))))"""


# Quiz of the day solution by Prince
# print fibbonaci series with the help of function
def fibb(n):
    a=-1
    b=1

    for i in range(n):
        fib=a+b
        print(fib,end=' ')
        a=b
        b=fib

fibb(int(input("Enter number you want to print fibbonaci : ")))
