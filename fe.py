import io
import os
import sys


def refresh_file(filename):
    # Check if the file path exists
    if os.path.exists(filename):
        with open(filename, "w") as f:
            # Clear the contents of the file
            f.truncate(0)
    else:
        # Print error message if the file path does not exist
        print("File path does not exist.")


def log_events(event, filename="/home/saved/temp.txt"):
    try:
        # get the directory from the filename
        directory = os.path.dirname(filename)

        # Create the directory if it does not exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create the file if it does not exist
        if not os.path.exists(filename):
            open(filename, "w").close()

        # Open the file in append mode
        with open(filename, "a") as f:
            # Write the event to the file with a newline
            f.write(event + "\n")
        return True
    except:
        # Return False if an exception occurs
        return False


def analyze_game(fobj):
    
    # Check if fobj is an instance of io.TextIOWrapper
    if not isinstance(fobj, io.TextIOWrapper):
        return ""
    # Initialise vairbales to store game data
    total_cheddar = 0
    total_spent = 0
    total_sound = 0
    total_brown = 0
    total_misses = 0
    total_forgot = 0
    total_revenue = 0
    in_game = False
    in_place = False
    end_game_encountered = False

    # Iterate over each line in fobj
    for line in fobj:
        line = line.strip()

        # Check for start and end of game and place markers
        if line == "Start game":
            in_game = True
        elif line == "End game":
            in_game = False
            end_game_encountered = True
        elif line.startswith("Start") and (line.endswith("shop") or line.endswith("hunt")):
            in_place = True
        elif line.startswith("End") and (line.endswith("shop") or line.endswith("hunt")):
            in_place = False

        # Process game data if in game and in place
        if in_game and in_place:

            if line.startswith("Bought"):
                cheddar_bought = int(line.split()[1])
                total_cheddar += cheddar_bought
                total_spent += cheddar_bought*10
            elif line.startswith("Caught"):

                if "Brown" in line:
                    total_brown += 1
                    total_revenue += 125
                total_sound += 1
            elif line == "Nothing happens.":
                total_misses += 1
                total_sound += 1
            elif line == "Nothing happens. You are out of cheese!":
                total_sound += 1
                total_forgot += 1

    # Reset the game data if the game is still in progress and there is no end game marker
    if in_game and not end_game_encountered:
        total_cheddar = 0
        total_spent = 0
        total_sound = 0
        total_brown = 0
        total_misses = 0
        total_forgot = 0
        total_revenue = 0

    # Format result with the game data
    result = f'''You have spent {total_spent} gold in The Cheese Shop.
 Total cheddar bought: {total_cheddar}
You have sounded the horn {total_sound} times during The Hunt.
 Total Brown mouse caught: {total_brown}
 Total empty catches: {total_misses}
 Total hunt without cheese: {total_forgot}
You have earned {total_revenue} gold from The Hunt.'''
    return result

def main(args):

    # Check for the correct number of arguments
    if len(args) < 2 :
        print("Format: python3 fe.py <name>")
        return ""
    else:
        name = args[1]
        filename = f"/home/saved/{name}.txt"
    try:
        with open(filename, "r") as f:
            result = analyze_game(f)
            print(result)
            return result
    except FileNotFoundError:
        return ""

if __name__ == "__main__":
    main(sys.argv)
