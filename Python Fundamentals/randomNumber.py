# Python program to generate a random number

import random

num = random.random()
print(num)

# Generating a random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)

# Generating a Random number using choice()
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(list1))
# prints a random item from the string
string = "striver"
print(random.choice(string))

# Generating a Random Number using randrange()
# using randrange() to generate in range from 20 to 50. The last parameter 3 is step size to skip three numbers when selecting.
print("A random number from range is : ", end="")
print(random.randrange(20, 80, 5))

# Generating a Random number using shuffle()
# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)