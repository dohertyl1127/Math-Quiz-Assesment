# functions
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

    # main routine

while True:
    questions = check_questions()
    print(questions, "questions")
