# Created by Ellie Le at 4/6/2022

# This program count the letter inside a text file.

# Create a function that count the letter
def CountLetter():
    while True:
        # Use a while loop to catch error if user enter wrong file name
        file = input("Please enter file name to process: ")
        try:
            # open file
            handle = open(file, 'r')
        except:
            # Prompt incorrect input and ask user to try again
            print("file name", file,"doesn't exist.")
            continue
        break

    # Read the file
    fhand = handle.read()
    # Split the file into words
    words = fhand.split()
    # Create an empty dictionary
    count = dict()

    # Loop through the word inside words list
    for word in words:

        # Loop through each letter inside each word
        for letter in word:

            # If the letter is not inside the dictionary, add the letter to it
            if letter not in count:
                count[letter] = 1

            # If the letter is already inside the dictionary, add one
            else:
                count[letter] += 1

    print(count)

CountLetter()
# Ask the user if they want to repeat the program
while True:
    repeat = input('Do you want to try another file?  (y or n) ')
    if repeat == 'y' or repeat == 'Y':
        CountLetter()
    elif repeat == 'n' or repeat == 'N':
        print('Thank you for playing.')
        break
    else:
        continue
