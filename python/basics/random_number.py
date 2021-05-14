import random

low = int(input("Lower bound: "))
up = int(input("Upper bound: "))

r = random.randint(low, up)

print("Randomly generated number equals ", r)
