trap = ('High Strain Steel Trap', 'Hot Tub Trap', 'Cardboard and Hook Trap')
picked_trap = None
cheddar = 0


# Phase 1: Travelling to the Meadow
def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")


def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    enter = input("Press Enter to travel to the Meadow...")
    if enter == "":
        print("Travelling to the Meadow...")
        print("Larry: This is your camp. Here you'll set up your mouse trap.")
        return enter
    else:
        return False


# Phase 2: Setting up a trap
def setup_trap(trap: tuple) -> bool:
    print("Larry: Let's get your first trap...")
    enter = input("Press Enter to view traps that Larry is holding...")
    if enter == "":
        print("Larry is holding...")
        print("Left:", trap[0])
        print("Right:", trap[1])
    else:
        return False
    what_trap = input('Select a trap by typing "left" or "right": ').strip()
    if what_trap == 'left':
        print("Larry: Excellent choice.")
        print('Your "', trap[0], '" is now set!', sep = '')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        cheddar = True
        trap = trap[0]
    elif what_trap == 'right':
        print("Larry: Excellent choice.")
        print('Your "', trap[1], '" is now set!', sep='')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        cheddar = True
        trap = trap[1]
    else:
        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
        cheddar = False
        trap = trap[2]
    return trap, cheddar


# Phase 3: Sound the horn
def basic_hunt(trap, cheddar):
    print("Sound the horn to call for the mouse...")
    horn = input('Sound the horn by typing "yes": ')
    if horn == 'yes' and cheddar:
        print("Caught a Brown mouse!")
        print("Congratulations. Ye have completed the training.")
        return True
    elif horn != 'yes' and cheddar:
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!")
        return False
    elif horn == 'yes' and not cheddar:
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!")
        return False
    elif horn != 'yes' and not cheddar:
        print("Nothing happens.")
        return False


def hunt_status(basic_hunt):
    status = basic_hunt(trap, cheddar)
    if status:
        return True
    else:
        return False


def end(status: bool):
    if status == True:
        print("Good luck~")
        return True
    elif status == False:
        return False

def main():
    intro()
    travel_to_camp()
    result = setup_trap(trap)
    hunt_result = basic_hunt(result[0], result[1])
    hunt_status = end(hunt_result)
    return result


if __name__ == '__main__':
    main()
