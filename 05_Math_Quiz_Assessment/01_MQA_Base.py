# imports
import random
import math


# functions
def statement_gen(statement, decoration, ):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def instructions():
    print("Instructions go here")
    print()


def yes_no(question):
    while True:

        # ask user if they have played before
        response = input(question).lower()

        # if yes continue code
        if response == "yes" or response == "y":
            return "yes"
        # if no display instructions
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please choose yes/no")


def difficulty_checker():
    diff_level = ""
    while diff_level == "":

        level = input("Please enter the difficulty level (easy, medium, hard): ")

        if level.lower() == "easy" or level.lower() == "e":
            diff_level = "easy"
            break
            # Perform actions for Easy level here
        elif level.lower() == "medium" or level.lower() == "m":
            diff_level = "medium"
            break
            # Perform actions for Medium level here
        elif level.lower() == "hard" or level.lower() == "h":
            diff_level = "hard"
            break
            # Perform actions for Hard level here
        else:
            print("Invalid difficulty level entered. Please try again.")
            # Optionally, you can choose to recursively call the function again to prompt for a valid difficulty level
            # difficulty_checker()
    return diff_level


def check_questions():
    while True:
        response = input("how many questions? ")

        round_error = "please type either <enter>" \
                      "or an integer that is more than 0"

        if response != "":
            try:

                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here
# prints a game title
statement_gen("Welcome to my math quiz!", "=")
# ask user if they have played before and explains if not
print()
instruct = yes_no("Have you played before?")
print()

if instruct == "no":
    instructions()
# asks user for level of difficulty
difficulty_checker()
# asks user for amount of questions
questions = check_questions()
print(f"you will be asked {questions} questions")
print()
# set question amounts
questions_played = 0
questions_wrong = 0
questions_right = questions_played - questions_wrong
game_summary = []
