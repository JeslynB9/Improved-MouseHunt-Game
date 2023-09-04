import q4
gold = 125


def main():
    q4.intro()
    q4.travel_to_camp()
    while True:
        result = q4.setup_trap(q4.trap)
        trap, cheddar = result
        q4.hunt_result = q4.basic_hunt(result[0], result[1])
        hunt_status = q4.end(q4.hunt_result)
        play_again = input('\nPress Enter to continue training and "no" to stop training: ')
        if play_again == "":
            continue
        if play_again == "no":
            return trap, cheddar


if __name__ == '__main__':
    main()
