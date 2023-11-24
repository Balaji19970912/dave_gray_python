f = open('anime_char.txt')

# print(f.read(4))
# print(f.readline())

for line in f:
    print(line)
f.close()

try:
    f = open('anime_names.txt')
    print(f.read())
except:
    print("File Not Found!")
finally:
    print("I'll run anyway!")
    f.close()

try:
    f = open('movie_names.txt','a')
    f.write('Sky Fall')
except:
    print("ERROR!")
finally:
    print('I\'ll run anyway!')
    f.close()