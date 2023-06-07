# functions
def ask_questions():
    while True:

        response = input("how many questions? ")

        question_error = "please type either <enter>" \
                      "or an integer that is more than 0"

        if response != "":
            try:

                response = int(response)

                if response < 1:
                    print(question_error)
                    continue

            except ValueError:
                print(question_error)
                continue

        return response



# main routine

questions = ask_questions()
print(questions)