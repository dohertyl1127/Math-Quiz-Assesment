def statement_gen(statement, decoration,):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# main routine
statement_gen("Welcome to my math quiz!", "=")
statement_gen("You got it right!", "+")
statement_gen("You got it wrong", "#")
statement_gen("Game summary", "*")
