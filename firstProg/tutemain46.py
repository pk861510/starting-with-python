def prince(str1):
    print(f"Ye string harry ko de do { str1}")

def fault(a,b):
    return a+b+5
print(f"And the name is {__name__}") # name give __main__ bcz we acces this from tutemain46 in same file

if __name__ == '__main__':  # if we can not this than all code of this block is printed by tutemain2.py bcz we import tutemain46 in tutemain2

    prince("Kaliya")
    fault_value = fault(5,7)
    print(fault_value)

# this block of code under main can not access by other file we can use only in this file