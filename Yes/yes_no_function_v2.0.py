# Yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, display instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise, show error
        else:
            print("Please use either 'yes' or 'no'")


# Main Routine
show_instructions = yes_no("Have you played this game before? ")
print(f"You entered {show_instructions}")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")
