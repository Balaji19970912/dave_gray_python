import os
os.system("clear")

def add_one(num):
    # total = 0
    if(num >= 9):
        return num+1
    total = num + 1
    print(total)
    return add_one(total)

res = add_one(0)

print("Res = ",res)