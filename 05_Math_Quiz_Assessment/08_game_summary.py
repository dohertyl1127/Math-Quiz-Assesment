# functions
def game_summary(attempted, right, wrong):

    percent_right = right / attempted * 100
    percent_wrong = wrong / attempted * 100

    print(f"right: {right} ({round(percent_right, 2)}%) ")
    print(f"wrong: {wrong} ({round(percent_wrong, 2)}%) ")
    print()


# main routine
game_summary(5, 3, 2)
