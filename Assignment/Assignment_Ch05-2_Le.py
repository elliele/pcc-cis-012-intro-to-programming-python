# Created by Ellie Le at 2/14/2022

# This program calculates the sum of even and odd integers from six given numbers.

# Create a function to calculate the sum of even and odd integers
def CalculateSum():
    even_sum = 0
    odd_sum = 0

    n = 0
    print("Please enter 6 integers:")
    while n < 6:
        # Prompts the user for the six different numbers
        number = int(input())

        # Check if the number is even or odd
        if (number % 2) == 0:
            even_sum += number
        else:
            odd_sum += number

        # Use a counter to stop the loop
        n += 1

    print("\nEven sum:", even_sum)
    print("Odd sum:", odd_sum,"\n")

CalculateSum()

while True:
    # Prompt the user if they want to repeat the program
    repeat = input("Do you wish to repeat this program? (y/n) \n")

    # if the user answer "y", repeat the program
    if repeat == "y":
        print("\n")
        CalculateSum()
        continue

    # if the user answer "n", exit out of the program
    elif repeat == "n":
        break

print("\nDone!")


