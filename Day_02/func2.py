import os

os.system("clear")

def sumCheck(num1=0, num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

res = sumCheck(10,12)

print(res)
