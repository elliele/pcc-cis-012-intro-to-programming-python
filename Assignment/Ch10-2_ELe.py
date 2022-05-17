# Created by Ellie Le at 4/13/2022

# This program will take a file name from user and read the lines that begin with "From".
# Then it will pull out the email address and count the number of messages from each email address.
# The program will print out a list with the most frequent number of email address in a list.

import re

def EmailLookup():

    while True:
        # Use a while loop to catch error if user enter wrong file name
        file = input("Enter file name to process: ")
        try:
            # open file
            handle = open(file, 'r')

        except:
            # Prompt incorrect input and ask user to try again
            print("File", file, "doesn't exist.")
            print("Please enter correct file name")
            continue
        break

    # Create an empty dictionary
    count = dict()

    for line in handle:
        line = line.rstrip()
        # Search for all email begin with 'From
        if re.search('^From', line):
            # Find the email address within research
            i = re.findall('(\S+@\S+)',line)
            for email in i:
                if email not in count:
                    # if the email is not in the dictionary, add them to the dictionary
                    count[email] = 1
                else:
                    # If the email is already inside the dictionary, add one
                    count[email] += 1


    print("Here is a list of top 5 email users:")
    # Sort the email dictionary by value in descending order using sorted reverse =True
    email_list = sorted(((v, k) for (k, v) in count.items()), reverse=True)
    # Print the top 5 email list
    print(email_list[:5])


EmailLookup()

# Ask the user if the want to repeat the program
while True:
    repeat = input('Do you want to continue?  (y or n) ')
    if repeat == 'y' or repeat == 'Y':
        EmailLookup()
    elif repeat == 'n' or repeat == 'N':
        print('Thank you for playing.')
        break
    else:
        continue
