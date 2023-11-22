x = 2

try:
    x / 1
except NameError:
    print("It's a name error!")
except ZeroDivisionError:
    print("Cannot divide a number by zero!")
else:
    print('Yo')
finally:
    print("How to do that!")