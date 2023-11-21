def parent_function(person,coins):
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n"+str(person)+" has "+str(coins) + " coins")
        elif coins == 1:
            print("\n"+str(person)+" has "+str(coins) + " coins")
        else:
            print("\n"+str(person)+" is out of coins")
    return play_game

tommy = parent_function("tommy",3)
jenny = parent_function("jenny",5)

tommy()
jenny()