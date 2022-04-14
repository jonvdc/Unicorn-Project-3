import random

tokens = ["unicorn", "donkey", "horse", "zebra"]

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # can wrap output making it easier to screenshot
