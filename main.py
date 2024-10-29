import random
import time
import json



def save_results(name="unnamed", attemts=None, time_of_game=None, level=None):
    file = open("results.txt", "a")
    results_of_user = json.dumps({"name" : name, "difficult" : level, "attemts":attemts, "time_of_game":time_of_game, "level":level})
    file.write('\n'+results_of_user)
    file.close()

def show_leaderboard():
    with open("results.txt", "r") as file:
        for line in file:
            if line.strip():
                results_of_user = json.loads(line)
                print("Player:", results_of_user['name'])
                print("Attempts:", results_of_user['attemts'])
                print("Time in game (seconds):", results_of_user['time_of_game'])
                print("The level was:", results_of_user['level'])
                print("-" * 30)


def game(chances,level,custom=0,high_number=100):

    if custom==1:
        high_number=int(input("Please enter the high number for generation:\n"))
        unknown_digit = random.randint(1, high_number)
    elif custom==0:
        unknown_digit = random.randint(1, 100)
    attempts = 0

    name = input("Please enter your name:\n")
    start_time = time.time()

    while attempts < chances:
        entered_digit = input("Enter the digit:\n")

        if entered_digit == "Exit" or entered_digit == "exit":
            print(f"You quit the game. The guessed number was {unknown_digit}.")
            return

        try:
            entered_digit = int(entered_digit)
        except ValueError:
            print("Invalid input. Please enter a digit or 'Exit'.")
            continue

        attempts += 1

        if entered_digit == unknown_digit:
            end_time = time.time()
            time_of_game=end_time-start_time
            time_of_game=int(time_of_game)
            print(f"Congratulations! {name} guessed the correct number in {attempts} attempts and in {time_of_game} seconds.")
            save_results(name,attempts,time_of_game,level)

            return

        elif entered_digit > unknown_digit:
            print(f"Entered digit {entered_digit} is more than the unknown digit.")
        elif entered_digit < unknown_digit:
            print(f"Entered digit {entered_digit} is less than the unknown digit.")

    print(f"{name} lost. The guessed number was {unknown_digit}.")


def print_help_text():
    print("Welcome to Number-Guessing-Game-on-Python"
          "\nEnter 1 for easy level"
          "\nEnter 2 for medium level"
          "\nEnter 3 for hard level"
          "\nEnter 4 for unlimited level"
          "\nEnter 5 for custom level"
          "\nEnter 7 for help"
          "\nEnter 8 for show a leaderboard"
          "\nEnter 0 for exit ")

while True:
    print_help_text()
    while True:
        action = int(input("Enter your action:\n"))
        if action == 1:
            print("Great!You select a easy level")
            game(chances=10,level='Easy level')
        elif action == 2:
            print("Great!You select a medium level")
            game(chances=5,level='Medium level')
        elif action == 3:
            print("Great!You select a hard level")
            game(chances=3,level='Hard level')
        elif action == 4:
            print("Great!You select a unlimited level")
            game(chances=999999,level='Unlimited level')
        elif action == 5:
            print("Great!You select a custom level")
            game(chances=int(input("Please enter the amount of chances:\n")), level='Custom level',custom=1)
        elif action == 7:
            print_help_text()
        elif action == 8:
            show_leaderboard()
        elif action == 0:
            exit()
        else:
            print("Something gone wrong.")
