import random


# functions
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


def check_answer(equation, answer, max_attempts):
    for item in range(max_attempts + 1):
        user_answer = input(equation)
        if user_answer == answer:
            print("Correct!")
            return True
        else:
            print(f"Attempt {attempt} is incorrect.")
        print("Sorry, you've used all your attempts. The correct answer was:", answer)
        return False


# main routine
while True:
    diff_level = difficulty_checker()

    print(f"you select {diff_level} difficulty")
    print()

    questions = check_questions()
    print(questions, "questions")

    for item in range(questions):
        equation, answer = generate_random_equation()
        print("Equation:", equation)
        print("Answer:", answer)
        if diff_level == 'easy':
            max_attempts = 4
        else:
            max_attempts = 2
        check_answer(equation, answer, max_attempts)
