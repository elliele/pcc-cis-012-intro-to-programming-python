# Created by Ellie Le at 4/6/2022

# This program take a file from the user and count the word inside the file.
# All the word will be in lowercase and excluding special characters.
# The program will then print the word and occurrences of word in alphabetical order.


def CountWord():
    while True:
        # Use a while loop to catch error if user enter wrong file name
        file_name = input("Please enter file name: ")
        try:
            # open file
            handle = open(file_name, 'r')
        except:
            # Prompt incorrect input and ask user to try again
            print("File name", file_name,"cannot be found")
            continue
        break


    # Change all the words to lowercase
    fhand = handle.read().lower()
    words = fhand.split()

    # Create an empty dictionary
    count = dict()
    for word in words:
        word = word.strip('.,!;:[]()')
        # if the word is not in the dictionary, add them to the dictionary
        if word not in count:
            count[word] = 1
        # # If the letter is already inside the dictionary, add one
        else:
            count[word] += 1


    print("Words and frequency in the file", file_name, "sorted alphabetically")
    # Sort the dictionary in alphabetical order
    for i in sorted(count):
        print(i,count[i])
    print("There are",len(count),"different words in the file.")



CountWord()
# Ask the user if they want to repeat the program
while True:
    repeat = input('Do you want to try another file?  (y or n) ')
    if repeat == 'y' or repeat == 'Y':
        CountWord()
    elif repeat == 'n' or repeat == 'N':
        print('Thank you for playing.')
        break
    else:
        continue
