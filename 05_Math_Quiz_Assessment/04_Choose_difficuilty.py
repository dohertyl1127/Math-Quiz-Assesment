# Functions
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

    print(f"you select {diff_level} difficulty")
    print()


# Call the function
while True:
    difficulty_checker()
