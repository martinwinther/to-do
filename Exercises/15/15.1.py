import random

# Get two numbers from the user and covert them to integers
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Pick a random int using randrange()
rand = random.randrange(lower_bound, upper_bound + 1) # We add 1 to upper_bound because randrange does not include the upper_bound number.

print(rand)