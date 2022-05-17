# Created by Ellie Le at 3/29/2022

# This program take a file name from the user and find all the unique words within the file.
# The list will be sorted in alphabetical orders and state how many words are found.
# This program will also ask the user if they want to repeat the program



def ExtractWord():
    # Use a while loop to catch error
    while True:
        file = input("Enter file name: ")
        try:
            # open file
            handle = open(file, 'r')
        except:
            # Prompt incorrect input and ask user to try again
            print("file not found, please enter correct file name.")
            continue
        else:
            break

    # Create empty list
    word_list = []
    count = 0

    # Read the file and convert and split all words in lower case
    fhand = handle.read()
    fhand = fhand.lower()
    words = fhand.split()

    # Loop through the words
    for word in words:
        word = word.strip('.,!;[]()')

        # if the word is not in the list, add them to the word_list
        if word not in word_list:
            word_list.append(word)
            count += 1

    # Print the result
    print(sorted(word_list))
    print("File", file, 'has', count, 'words')

ExtractWord()

# Ask the user if they want to repeat the program
while True:
    repeat = input('Do you want to try another file? (y or n) ')
    if repeat == 'y':
        ExtractWord()
    elif repeat == 'n':
        print('Thank you for playing.')
        break
