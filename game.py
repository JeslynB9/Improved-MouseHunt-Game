'''
Answer for Question 7 - PIAT: The Hunt

Name: Jeslyn Joylie Bowman
SID: 530481526
unikey: jbow2146

'''

import random
import q1
import train
import shop
from name import is_valid_name
import q4
import os
import shutil

gold = 0
cheese = 0
points = 0

def log_events(event):
    with open("/home/saved/temp.txt", "a") as f:
        f.write(event + "\n")


def greeting():
    print(q1.splash)
    print("\nWhat's ye name, Hunter?")


def start_game(name):
    open("/home/saved/temp.txt", "w").close()
    start = input('Press "Enter" to start training or "skip" to Start Game: ')
    if start == 'skip':
        trap = "Cardboard and Hook Trap"
        return trap
    else:
        print('')
        trap, cheddar = train.main()
        return trap


def game_menu(gold, cheese, trap, name_first, points):
    if not is_valid_name(name_first):
        name = "Bob"
    else:
        name = name_first
    log_events("Start game")
    while True:
        print("\nWhat do ye want to do now, Hunter ", name, "?", sep = '')
        print("1. Exit game\n2. Join the Hunt\n3. The Cheese Shop")
        what_choice = input()
        if what_choice == '1':
            log_events("End game")
            if is_valid_name(name_first):
                shutil.copy("/home/saved/temp.txt", f"/home/saved/{name_first}.txt")
                return
            else:
                return
        elif what_choice == '2':
            log_events("Start hunt")
            gold, points, cheese = join_hunt(gold, cheese, points)
            log_events("End hunt")
        elif what_choice == '3':
            log_events("Start shop")
            gold, cheese = shop.main(gold, cheese, trap)
            log_events(f"Bought {cheese} cheddar")
            log_events("End shop")


def join_hunt(gold, cheese, points):
    i = 0
    while i < 5:
        print("Sound the horn to call for the mouse...")
        horn = input('Sound the horn by typing "yes": ')
        if horn == 'yes' and cheese >= 1:
            chance = random.random()
            if chance <= 0.5:
                print("Caught a Brown mouse!")
                gold = gold + 125
                points = points + 115
                cheese = cheese - 1
                print("My gold: ", gold, ", " "My points: ", points, sep = '', end = '\n\n')
                i = 0
                log_events("Caught a Brown mouse!")
            elif chance > 0.5:
                print("Nothing happens.")
                cheese = cheese - 1
                print("My gold: ", gold, ", " "My points: ", points, sep = '', end = '\n\n')
                i += 1
                log_events("Nothing happens.")
        elif horn == 'yes' and cheese == 0:
            print("Nothing happens. You are out of cheese!")
            print("My gold: ", gold, ", " "My points: ", points, sep = '', end = '\n\n')
            i += 1
            log_events("Nothing happens. You are out of cheese!")
        elif horn == 'stop hunt':
            return gold, points, cheese
        else:
            i += 1
            print("Do nothing.")
            print("My gold: ", gold, ", " "My points: ", points, sep = '', end = '\n\n')
            log_events("Do nothing")
        if i >= 5:
            continue_hunt = input("Do you want to continue to hunt? ")
            if continue_hunt == 'no':
                log_events("End hunt")
                return gold, points, cheese
            else:
                i = 0


def buy_cheese(gold, log_events):
    while True:
        print("You have", gold, "gold to spend.")
        cheese_quantity = input("State [cheese quantity]: ").lower().split()
        if len(cheese_quantity) != 2 or cheese_quantity[0] != 'cheddar':
            if cheese_quantity == ['back']:
                return 0, 0
            else:
                print("Sorry, did not understand.")
                return 0, 0
        else:
            cheese = cheese_quantity[0]
            try:
                quantity = int(cheese_quantity[1])
            except (IndexError, ValueError):
                return None
            quantity = int(cheese_quantity[1])
            if quantity <= 0:
                print("Must purchase a positive amount of cheese.")
                return 0, 0
            elif gold < quantity*10:
                print("Insufficient gold.")
                return 0, 0
            else:
                gold_spent = quantity*10
                gold -= gold_spent
                print("Successfully purchase", quantity, "cheddar.")
                return gold_spent, quantity


def inventory(gold, cheese, trap):
    print("Gold -", gold)
    print("Cheddar -", cheese)
    print("Trap -", trap)


def cheese_shop(trap, cheese, gold):
    log_events("Start shop")
    print("Welcome to The Cheese Shop!")
    print("Cheddar - 10 gold")
    while True:
        print("\nHow can I help ye?")
        print("1. Buy cheese\n2. View inventory\n3. Leave shop")
        shop_choice = input()
        if shop_choice == '1':
            gold_spent, quantity = buy_cheese(gold)
            if quantity == 0:
                continue
            else:
                gold -= gold_spent
                cheese += quantity
        elif shop_choice == '2':
            if trap == 'left':
                trap = "High Strain Steel Trap"
            elif trap == 'right':
                trap = "Hot Tub Trap"
            else:
                trap = "Cardboard and Hook Trap"
            inventory(gold, cheese, trap)
        elif shop_choice == '3':
            log_events("End shop")
            return shop_choice


def main():
    trap = ('High Strain Steel Trap', 'Hot Tub Trap', 'Cardboard and Hook Trap')
    gold = 125
    cheese = 0
    points = 0
    greeting()
    name_first = input()
    if is_valid_name(name_first):
        name = name_first
        print("Welcome to the Kingdom, Hunter ", name, "!", sep = '')
    else:
        name = 'Bob'
        print("Welcome to the Kingdom, Hunter ", name, "!", sep = '')
    print("Before we begin, let's train you up!")
    trap = start_game(name)
    game_menu(gold, cheese, trap, name_first, points)


if __name__ == '__main__':
    main()