# imports
import random


# Function to check if user input is an integer
def int_checker(question):
    while True:
        user_input = input(question)
        if user_input == "xxx":  # If the user enters 'xxx', they want to exit the program
            end = "exit"
            return end
        try:
            number = float(user_input)  # Try to convert user input to a float
            return number  # Return the converted number if successful
        except ValueError:
            print("Invalid input. Please enter a number.")
            # The input was not a valid number, so ask the user to enter a number again


# Function to generate a statement with decoration
def statement_gen(statement, decoration):
    sides = decoration * 3  # Repeat the decoration character 3 times to create sides
    statement = "{} {} {}".format(sides, statement, sides)  # Add the sides to the statement
    top_bottom = decoration * len(statement)  # Create a top/bottom decoration based on the statement's length
    print(top_bottom)
    print(statement)
    print(top_bottom)


# Function to display instructions
def instructions():
    print("This is a basic math quiz. In this quiz, you will choose from ")
    print("easy, medium, and hard difficulties. Then, choose how many")
    print("questions you will be asked. I would recommend easy for 0-10")
    print("year olds, medium for 11-15 year olds and hard for 16+. Try to ")
    print("answer the questions to the best of your ability and have fun!")
    print()


# Function to prompt for a yes or no response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"  # Return 'yes' if the user input indicates affirmation
        elif response == "no" or response == "n":
            return "no"  # Return 'no' if the user input indicates negation
        else:
            print("Please choose yes/no")  # The user input was neither 'yes' nor 'no', ask again


# Function to validate and return the difficulty level chosen
def difficulty_checker():
    diff_level = ""
    while diff_level == "":
        level = input("Please enter the difficulty level (easy, medium, hard): ")
        # if user asks for easy difficulty set diff_level to easy
        if level.lower() == "easy" or level.lower() == "e":
            diff_level = "easy"
            break
        # if user asks for medium difficulty set diff_level to medium
        elif level.lower() == "medium" or level.lower() == "m":
            diff_level = "medium"
            break
        # if user asks for hard difficulty set diff_level to hard
        elif level.lower() == "hard" or level.lower() == "h":
            diff_level = "hard"
            break
        # if invalid input print invalid response
        else:
            print("Invalid difficulty level entered. Please try again.")
    return diff_level


# Function to check the number of questions input by the user
def check_questions():
    while True:
        response = int_checker("How many questions? ")
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
    # generates easy numbers and operators
    if diff_level == "easy":
        operators = ['+', '-']
    else:
        operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    if diff_level == "easy":
        operand1 = random.randint(1, 50)
        operand2 = random.randint(1, 50)
    # generates medium numbers and operators
    elif diff_level == "medium":
        if operator == '*':
            operand1 = random.randint(1, 20)
            operand2 = random.randint(1, 20)
        elif operator == '/':
            operand2 = random.randint(1, 50)
            operand1 = random.randint(1, 50) * operand2
        else:
            operand1 = random.randint(1, 1000)
            operand2 = random.randint(1, 1000)
    # generates hard numbers and operators
    else:
        if operator == '*':
            operand1 = random.randint(1, 100)
            operand2 = random.randint(1, 100)
        elif operator == '/':
            operand2 = random.randint(1, 100)
            operand1 = random.randint(1, 100) * operand2
        else:
            operand1 = random.randint(1, 10000)
            operand2 = random.randint(1, 10000)
    # Calculate the correct answer based on the chosen equation
    if operator == '+':
        correct_answer = operand1 + operand2
    elif operator == '-':
        correct_answer = operand1 - operand2
    elif operator == '*':
        correct_answer = operand1 * operand2
    else:
        correct_answer = operand1 / operand2

    # Create a printable equation string and return both the equation and the correct answer
    print_equation = f"{operand1} {operator} {operand2}"
    return print_equation, correct_answer


# Function to check if the user's answer is correct
def check_answer(question, correct_answer, difficulty):
    # sets attempts depending on the difficulty
    if difficulty == 'easy':
        attempts = 3
    else:
        attempts = 2
    attempts_taken = 0
    attempts_left = attempts
    # give the user their attempts
    for i in range(attempts):
        wrong = "Sorry, that is incorrect"
        attempts_left -= 1
        print(f"You have {attempts_left + 1} attempts")
        user_answer = int_checker(f"{question} = ")
        if user_answer == correct_answer:
            return 'correct'  # The user's answer is correct, return 'correct'
        elif user_answer == "exit":
            return 'exit'  # The user wants to exit the quiz, return 'exit'
        elif attempts_left < 1:
            return 'wrong'  # The user has run out of attempts, return 'wrong'
        else:
            print(wrong)
            attempts_taken += 1


# Function to display the game summary
def game_summary(attempted, right, wrong):
    # makes sure that 1<= questions have been answered and then does the necessary math
    if attempted >= 1:
        percent_right = right / attempted * 100
        percent_wrong = wrong / attempted * 100
        print(f"Wins: {right} ({round(percent_right, 2)}%)")
        print(f"Loss: {wrong} ({round(percent_wrong, 2)}%)")
    # if 1> answers have been asked say that there is no game history
    else:
        print("there is no game history ")


# Main routine
questions_attempted = 0
questions_wrong = 0
questions_right = 0

# Prints the game title
statement_gen("Welcome to my math quiz!", "=")

# Asks the user if they have played before and provides instructions if not
print()
instruct = yes_no("Have you played before?")
print()
# prints instructions if user has not played before
if instruct == "no":
    statement_gen("Instructions: ", "*")
    print()
    instructions()

# Asks the user for the level of difficulty
diff_level = difficulty_checker()
print(f"you choose {diff_level} difficulty")
print()
# Asks the user for the number of questions
questions = check_questions()
print(f"You will be asked {questions} questions")
print()

# Loop to generate and check each question
for item in range(questions):
    equation, answer = generate_random_equation()
    statement_gen(f"Question {questions_attempted + 1} of {questions}", "=")
    wrong_right = check_answer(equation, answer, diff_level)
    # if users input is an exit command stop program
    if wrong_right == 'exit':
        break
    # if user enters correct answer print that they are correct and add one to right tally
    elif wrong_right == 'correct':
        statement_gen("Correct!", "+")
        questions_right += 1
    # if user uses all attempts and doesn't get the answer correct give tell them they are wrong and give correct
    # answer, add one to wrong tally
    elif wrong_right == 'wrong':
        statement_gen(f"Sorry, you got it wrong, the correct answer was {answer}", "-")
        questions_wrong += 1
    questions_attempted += 1
    print()

# Display game summary and thank user for playing
print()
statement_gen("Game Summary: ", "#")
print()
game_summary(questions_attempted, questions_right, questions_wrong)
print()
print("thanks for playing my math quiz! ")
