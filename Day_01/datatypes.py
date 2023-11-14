#constructor function

years = "World"
y = type(years)
print(isinstance(years,y))

#string functions

name = "Monkey D Luffy"
print(name.lower())
print(name.upper())
print(name.replace("Luffy",'Garp'))
print(name.title())
print(len(name))


#menu designing

title = "menu".upper()
print("\n",title.center(20,"="))
print("")
print("Pizza ".ljust(16,".")+"$1".rjust(4," "))
print("Pasta ".ljust(16,".")+"$1".rjust(4," "))
print("Burger ".ljust(16,".")+"$1".rjust(4," "))
print("Taco ".ljust(16,".")+"$1".rjust(4," "))

print(int("100"))