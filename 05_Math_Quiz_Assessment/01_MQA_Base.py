# imports
import random
import math


# Function to check if user input is an integer
def int_checker(question):
    while True:
        user_input = input(question)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to generate a statement with decoration
def statement_gen(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# Function to display instructions
def instructions():
    print("This is a basic math quiz. In this quiz, you will choose from ")
    print("easy, medium, and hard difficulties. Then, choose how many")
    print("questions you will be asked. Try to answer the questions to")
    print("the best of your ability and have fun!")
    print()


# Function to prompt for a yes or no response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please choose yes/no")


# Function to validate and return the difficulty level chosen
def difficulty_checker():
    diff_level = ""
    while diff_level == "":
        level = input("Please enter the difficulty level (easy, medium, hard): ")
        if level.lower() == "easy" or level.lower() == "e":
            diff_level = "easy"
            break
        elif level.lower() == "medium" or level.lower() == "m":
            diff_level = "medium"
            break
        elif level.lower() == "hard" or level.lower() == "h":
            diff_level = "hard"
            break
        else:
            print("Invalid difficulty level entered. Please try again.")
    return diff_level


# Function to check the number of questions input by the user
def check_questions():
    while True:
        response = input("How many questions? ")
        round_error = "Please type either <enter> or an integer that is more than 0"
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


# Function to generate a random equation based on difficulty level
def generate_random_equation():
    if diff_level == "easy":
        operators = ['+', '-']
        operator = random.choice(operators)
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)
    elif diff_level == "medium":
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)
        if operator == '/':
            denominator = random.randint(1, 10)
            numerator = random.randint(1, 10) * denominator
    elif diff_level == "hard":
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        operand1 = random.randint(1, 100)
        operand2 = random.randint(1, 100)
        if operator == '/':
            denominator = random.randint(1, 100)
            numerator = random.randint(1, 100) * denominator
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


# Function to check if the user's answer is correct
def check_answer(question, correct_answer, difficulty):
    if difficulty == 'easy':
        attempts = 4
    else:
        attempts = 2
    attempts_taken = 0
    attempts_left = attempts
    for item in range(attempts):
        wrong = "Sorry, that is incorrect"
        attempts_left -= 1
        print(f"You have {attempts_left + 1} attempts")
        user_answer = int_checker(question)
        if user_answer == correct_answer:
            return 'correct'
        elif attempts_left < 1:
            return 'wrong'
        else:
            print(wrong)
            attempts_taken += 1


# Function to display the game summary
def game_summary(attempted, right, wrong):
    percent_right = right / attempted * 100
    percent_wrong = wrong / attempted * 100
    print(f"Wins: {right} ({round(percent_right, 2)}%)")
    print(f"Loss: {wrong} ({round(percent_wrong, 2)}%)")


# Main routine
questions_attempted = 0
questions_wrong = 0
questions_right = questions_attempted - questions_wrong

# Prints the game title
statement_gen("Welcome to my math quiz!", "=")

# Asks the user if they have played before and provides instructions if not
print()
instruct = yes_no("Have you played before?")
print()

if instruct == "no":
    statement_gen("Instructions: ", "*")
    print()
    instructions()

# Asks the user for the level of difficulty
diff_level = difficulty_checker()

# Asks the user for the number of questions
questions = check_questions()
print(f"You will be asked {questions} questions")
print()

# Loop to generate and check each question
for item in range(questions):
    equation, answer = generate_random_equation()
    statement_gen(f"Question {questions_attempted + 1} of {questions}", "=")
    wrong_right = check_answer(equation, answer, diff_level)
    if wrong_right == 'correct':
        statement_gen("Correct!", "+")
        questions_right += 1
    elif wrong_right == 'wrong':
        statement_gen("Sorry, you got it wrong", "-")
        questions_wrong += 1
    questions_attempted += 1
    print()

# Display game summary
statement_gen("Game Summary: ", "#")
game_summary(questions_attempted, questions_right, questions_wrong)
