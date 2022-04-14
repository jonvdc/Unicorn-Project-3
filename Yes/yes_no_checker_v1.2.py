# Ask the user if they have played before
show_instructions = input("Have you played this game before?: ").lower()

# If they say yes, program continues
if show_instructions == "yes" or show_instructions == "y":
    print("Program continues")

# If they say no, display instructions
elif show_instructions == "no" or show_instructions == "n":
    print ("Show instructions")

# Otherwise, show error
else:
    print("Please use either 'yes' or 'no'")

print(f"You entered {show_instructions}")
