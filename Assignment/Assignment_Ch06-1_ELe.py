# Created by Ellie Le at 3/8/2022


# This program take a string as an input and extract a string after a colon.
# Then it will convert it to floating point number and add 2.0 to it.

# Prompt user for a string with a colon and a number after it
user = input("Enter a string with a colon and a number after it: ")

# Find the position of the colon within the string
position = user.find(':')

# Convert the string to floating point number and add 2.0 to it
result = float(user[position+1:]) + 2.0

print("Extracted a number from given string and added 2.0 to it:", result)
