def int_checker():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


# Example usage
while True:
    number = int_checker()
    print("You entered:", number)
