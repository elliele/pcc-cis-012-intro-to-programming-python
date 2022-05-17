# Created by Ellie Le at 3/29/2022


# This program will take a file name from the user and find the following information and display it.
# The information needed are the number of lines, number of vowels, number of constants, and number of characters.

# Create a function to count character in text file.
def CountCharacter():

    # Use a while loop to catch error
    while True:
        file = input("Please enter file name: ")

        try:
            # open file
            handle = open(file, 'r')
        except:
            # Prompt incorrect input and ask user to try again
            print("Incorrect input, please try again.")
            continue
        else:
            break


    lines = 0
    vowels = 0
    constants = 0
    number = 0
    count = 0
    constants_char = list('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    vowels_char = list('aeiouAEIOU')
    # use a for loop to loop through the text file
    for line in handle:

        # Count the number of lines
        lines += 1

        # loop through the word inside the lines of the text file
        for word in line:
            # if the word contains a vowel, add to the vowels count
            if word in vowels_char:
                vowels += 1

            # if the word contains a constant, add to constants count
            elif word in constants_char:
                constants += 1

            # if the word contains a number, add to the numerical characters count
            elif (word.isnumeric()):
                number += 1

    # Print the result
    print("File", file, "has", lines, "lines.")
    print("File", file, "has", vowels, "vowels.")
    print("File", file, "has", constants, "constants.")
    print("File", file, "has", number, "numerical characters.")


CountCharacter()

# Use a while loop to ask user if they want to repeat the program
while True:
    repeat = input("Do you want to try again? (y or n) ")
    if repeat == 'y':
        CountCharacter()
    elif repeat == 'n':
        print("Thanks for playing!")
        break
