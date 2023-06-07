# functions
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


# main routine
while True:
    instruct = yes_no("Have you played before?")
    print()

    if instruct == "no":
        instructions()

    print("program continues")