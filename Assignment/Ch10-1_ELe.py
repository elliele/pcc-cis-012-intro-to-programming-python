# Created by Ellie Le at 4/12/2022

# This program will take a file from the user and find out the number of occurrences for each alphabet.
# Uppercase and lowercase letter are counted as the same characters.
# The list will be sorted by ascending value.

# Create a function to count the alphabet

def CountAlphabet():
    while True:
        # Use a while loop to catch error if user enter wrong file name
        file = input("Please enter file name to process: ")
        try:
            # open file
            handle = open(file, 'r')

        except:
            # Prompt incorrect input and ask user to try again
            print("file name", file, "doesn't exist.")
            continue
        break

    punc = '@#$%^&*()!()-[]{};:\'\"\,<>./?@#$%^&*_~'
    # Create an empty dictionary
    count = dict()
    for lines in handle:
        # Delete the punctuation from the text file
        lines = lines.translate(lines.maketrans(" ", " ",punc))
        # Convert lines into lowercase character
        lines = lines.lower().split()
        for words in lines:
            for letter in words:
                # if the word is not in the dictionary, add them to the dictionary
                if letter not in count:
                    count[letter] = 1
                # If the letter is already inside the dictionary, add one
                else:
                    count[letter] += 1

    # Sort the tuple by value instead of key
    print(sorted((v,k) for k,v in count.items()))



CountAlphabet()

# Ask the user if they want to repeat the program
while True:
    repeat = input('Do you want to try another file?  (y or n) ')
    if repeat == 'y' or repeat == 'Y':
        CountAlphabet()
    elif repeat == 'n' or repeat == 'N':
        print('Thank you for playing.')
        break
    else:
        continue
