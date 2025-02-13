import random

# Create a list of 10 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)

# Get the number at the random index
suggestion = numbers[random_number]

# Display the suggestion
print(suggestion)

