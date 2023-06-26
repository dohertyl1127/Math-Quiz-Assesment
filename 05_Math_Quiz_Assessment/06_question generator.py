import random
# function
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


def question_gen(max, operater):
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    if operator == '/':
        # Ensure the division is exact by generating a random numerator and denominator
        denominator = random.randint(1, max)
        numerator = random.randint(1, max) * denominator
        equation = f"{numerator} {operator} {denominator}"
        answer = numerator // denominator
    else:
        # Generate two random operands
        operand1 = random.randint(1, max)
        operand2 = random.randint(1, max)
        equation = f"{operand1} {operator} {operand2}"

        # Calculate the answer based on the operator
        if operator == '+':
            answer = operand1 + operand2
        elif operator == '-':
            answer = operand1 - operand2
        elif operator == '*':
            answer = operand1 * operand2

    return equation, answer


# main routine
diff_level = difficulty_checker()

print(f"you select {diff_level} difficulty")
print()

questions = check_questions()
print(questions, "questions")

for item in range(1, questions):
    def_question_gen()