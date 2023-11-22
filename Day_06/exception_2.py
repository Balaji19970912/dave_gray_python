try:
    x = 2
    res = x + 2
    raise Exception("I'm a custom exception")
except Exception as error:
    print(error)
else:
    print("yoyo")
finally:
    print("I'm there")

print(res)