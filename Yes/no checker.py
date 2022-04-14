# Ask the user if they have played before
show_instructions = input("Have you played this game before? ")

# If they say yes, program continues
if show_instructions == "yes":
    print("Program continues")

# If they say no, display instructions
elif show_instructions == "no":
    print ("Show instructions")

# Otherwise, show error
else:
    print("Please use either 'yes' or 'no'")



