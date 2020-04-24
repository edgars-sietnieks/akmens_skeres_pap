import random
import os
import sys

opcijas = ["a", "s", "p"]
pc_choise = random.choice(opcijas)

def game():
    os.system('cls||clear')
    user_choise = input("a, s, p or q to exit ")
    if user_choise == "q":
        sys.exit()
    pc_choise = random.choice(opcijas)
    print("You: ", user_choise)
    print("PC: ", pc_choise)
    
    if user_choise == "a":
        
        if pc_choise == "a":
            print("niča")
        elif pc_choise == "s":
            print("tu uzvarēji")
        else:
            print("tu zaudēji")
        input()
        game()

    elif user_choise == "s":
        
        if pc_choise == "a":
            print("tu zaudēji")
        elif pc_choise == "s":
            print("niča")
        else:
            print("tu uzvarēji")
        input()
        game()
    elif user_choise == "p":
        
        if pc_choise == "a":
            print("tu uzvarēji")
        elif pc_choise == "s":
            print("tu zaudēji")
        else:
            print("niča")
        input()
        game()

    else:
        print("Cut the crap!!!")
        input()
        game()

game()