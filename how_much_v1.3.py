# Main routine
error = "That was not a valid input\n"
user_balance = 0

# Keep asking until a valid amount (1-10) is entered
while not valid:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much would you like to play with? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")
