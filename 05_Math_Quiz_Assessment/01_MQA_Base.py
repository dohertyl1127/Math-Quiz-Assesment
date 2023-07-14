# imports
import random
import math


# functions
def int_checker(question):
    while True:
        user_input = input(question)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


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


def generate_random_equation():
    if diff_level == "easy":
        operators = ['+', '-']
        operator = random.choice(operators)

        # Generate two random operands
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)
    elif diff_level == "medium":
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)

        # Generate two random operands
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)

        if operator == '/':
            # Ensure the division is exact by generating a random numerator and denominator
            denominator = random.randint(1, 10)
            numerator = random.randint(1, 10) * denominator
    elif diff_level == "hard":
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)

        # Generate two random operands
        operand1 = random.randint(1, 100)
        operand2 = random.randint(1, 100)

        if operator == '/':
            # Ensure the division is exact by generating a random numerator and denominator
            denominator = random.randint(1, 100)
            numerator = random.randint(1, 100) * denominator
    # define equation and answer
    equation = f"{operand1} {operator} {operand2}"
    if operator == '+':
        answer = operand1 + operand2
    elif operator == '-':
        answer = operand1 - operand2
    elif operator == '*':
        answer = operand1 * operand2
    elif operator == '/':
        equation = f"{numerator} {operator} {denominator}"
        answer = numerator // denominator

    return equation, answer


def check_answer(question, correct_answer, difficulty):
    if difficulty == 'easy':
        attempts = 4
    else:
        attempts = 2
    attempts_taken = 0
    attempts_left = attempts
    for item in range(attempts):
        wrong = "Sorry that is incorrect"
        attempts_left -= 1
        print(f"you have {attempts_left + 1} attempts ")
        user_answer = int_checker(question)
        if user_answer == correct_answer:
            return 'correct'
        elif attempts_left < 1:
            return 'wrong'
        else:
            print(wrong)
            attempts_taken += 1


def game_summary(attempted, right, wrong):

    percent_right = right / attempted * 100
    percent_wrong = wrong / attempted * 100

    print(f"right: {right} ({round(percent_right, 2)}%) ")
    print(f"wrong: {wrong} ({round(percent_wrong, 2)}%) ")
    print()


# Main routine goes here
# set question amounts
while end == "":
    questions_attempted = 0
    questions_wrong = 0
    questions_right = questions_attempted - questions_wrong
    # prints a game title
    statement_gen("Welcome to my math quiz!", "=")
    # ask user if they have played before and explains if not
    print()
    instruct = yes_no("Have you played before?")
    print()

    if instruct == "no":
        instructions()
    # asks user for level of difficulty
    diff_level = difficulty_checker()
    # asks user for amount of questions
    questions = check_questions()
    print(f"you will be asked {questions} questions")
    print()

    for item in range(questions):
        equation, answer = generate_random_equation()
        statement_gen(f"question {questions_attempted + 1} of {questions}", "=")
        wrong_right = check_answer(equation, answer, diff_level)
        if wrong_right == 'correct':
            statement_gen("correct!", "+")
            questions_right += 1
        elif wrong_right == 'wrong':
            statement_gen("sorry, you got it wrong", "-")
            questions_wrong += 1
        questions_attempted += 1
        print()
    statement_gen("Game Summary: ", "#")
    game_summary(questions_attempted, questions_right, questions_wrong)
    print("if you would like to play again press <enter> or xxx to exit")
