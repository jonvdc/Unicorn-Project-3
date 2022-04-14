user_balance = int(input("How much do you want to play with? (Must be an"
                         "integer between 1 and 10) $ "))

# Keep asking until a valid amount ($1 - $10) has been entered
while not 1 <= user_balance <= 10:
    print("Try again, please enter a whole number between 1 and 10")

print(f"You are playing with ${user_balance}")
