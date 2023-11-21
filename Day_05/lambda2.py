def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen)
print(addTwenty)

print(addTen(7))
print(addTwenty(7))