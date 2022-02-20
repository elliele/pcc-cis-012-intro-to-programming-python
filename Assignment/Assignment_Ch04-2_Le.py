# Created by Ellie Le at 2/9/2022
# This program will take three numbers from users and call a function to sort them in ascending order.
# Then display the result from the function


# Create a function that compare numbers
def Compare(a,b,c):

    # Check conditions statement and print integer numbers in ascending order
    if a < b and a < c and b < c:
        print("\nInput three integer numbers in ascending order: \n" + a, b, c)

    elif a < b and a < c and b > c:
        print("\nInput three integer numbers in ascending order: \n" , a, c, b)

    elif a > b and a < c and b < c:
        print("\nInput three integer numbers in ascending order: \n" + b, a, c)

    elif a < b and a > c and b > c:
        print("\nInput three integer numbers in ascending order: \n" + c, a, b)

    elif a > b and a > c and b > c:
        print("\nInput three integer numbers in ascending order: \n" + c, b, a)

    elif a > b and a > b and b < c:
        print("\nInput three integer numbers in ascending order: \n" + b, c, a)

    elif a > b and b == c:
        print("\nInput three integer numbers in ascending order: \n" + b, c, a)

    elif a == b and b < c:
        print("\nInput three integer numbers in ascending order: \n" + a, b, c)

    elif a < b and a == c:
        print("\nInput three integer numbers in ascending order: \n" + a, c, b)

    elif a > b and a == c:
        print("\nInput three integer numbers in ascending order: \n" + b, a, c)

    elif a == b and b == c:
        print("\nInput three integer numbers in ascending order: \n" + a, b, c)



# Prompts the user to input three numbers.
a = input("Please enter the first integer: ")
b = input("Please enter the second integer: ")
c = input("Please enter the third integer: ")
# Call the function
Compare(a,b,c)

