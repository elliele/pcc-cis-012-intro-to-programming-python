# Created by Ellie Le at 3/8/2022

# This program prompts user to enter a string with two "!" within it to mark substring.
# Then the program will output the substring in reverse order without the "!".

# Prompts the user to enter a string with two "!"
user = input("Enter a string with two \"!\" surrounding portion of the string: ")

# Find the position of the first "!"
begin = user.find("!")
# Find the position of the second "!"
end = user.find("!",begin+1)

# Print the substring in reverse order without the "!"
for i in user[end-1:begin:-1]:
    print(i)

# Create a while loop to repeat the program
while True:
    repeat = input("Do you want to try again? (y/n) ")
    if repeat == 'y':

        # Prompts the user for another string with two "!"
        prompt = input("Please enter a string with a word surrounded by !!: ")

        # Locate the position of the first and second "!" within the string
        begin1 = prompt.find("!")
        end1 = prompt.find("!", begin1 + 1)

        # Print the substring in reverse order
        for i in prompt[end1 - 1:begin1:-1]:
            print(i)

    # If user does not want to repeat the program, break out of the while loop
    elif repeat == 'n':
        print("Thank you for playing")
        break
