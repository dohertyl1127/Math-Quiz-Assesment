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


# Main routine goes here

statement_gen("Welcome to my math quiz!", "=")

print()
instruct = yes_no("Have you played before?")
print()

if instruct == "no":

    instructions()
