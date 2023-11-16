name = "luffy"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("luffy")
    # return 0

another()