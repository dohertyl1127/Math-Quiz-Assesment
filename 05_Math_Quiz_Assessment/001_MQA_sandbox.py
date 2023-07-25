import random


def generate_random_equation(diff_level="easy"):
    # generates operators
    if diff_level == "easy":
        operators = ['+', '-']
    else:
        operators = ['+', '-', '*', '/']

    operator = random.choices(operators, weights=[2, 2, 1, 1])[0]

    # generates operands based on the operator
    if operator == '+':
        operand1 = random.randint(1, 50)
        operand2 = random.randint(1, 50)
    elif operator == '-':
        operand1 = random.randint(1, 50)
        operand2 = random.randint(1, 50)
    elif operator == '*':
        operand1 = random.randint(1, 20) if diff_level == "medium" else random.randint(1, 100)
        operand2 = random.randint(1, 20) if diff_level == "medium" else random.randint(1, 100)
    else:
        operand2 = random.randint(2, 100) if diff_level == "medium" else random.randint(2, 10000)
        operand1 = random.randint(1, 100) * operand2

    # Create a printable equation string and return both the equation and the correct answer
    print_equation = f"{operand1} {operator} {operand2}"
    return print_equation, eval(print_equation)


# Example usage:
difficulty_level = "hard"
equation, correct_answer = generate_random_equation(diff_level=difficulty_level)
print("Equation:", equation)
print("Correct Answer:", correct_answer)
