# Created by Ellie Le at 2/14/2022


# This program takes a list of integers as input and use a "for" loop to calculate
# the sum of odd numbers, sum of even numbers, largest number and smallest number

lst = [3,8,5,1,4,9,2,10,7]

even_sum = 0
odd_sum = 0

smallest = None
largest = None

# Loop through the list
for i in lst:

    # If i is divisible by 2, then calculate sum of even numbers
    if (i % 2) == 0:
        even_sum += i

    # If i is not divisible by 2, then calculate sum of odd numbers
    else:
        odd_sum += i

    # The first time through the loop largest is None, so we take the first value to be the largest.
    if largest is None:
        largest= i
    # If i is greater than the current value, then i is now the new largest number.
    elif i > largest:
        largest = i

    # The first time through the loop smallest is None, so we take the first value to be the smallest.
    if smallest is None:
        smallest = i
    # If i is less than the current value, then i is now the new smallest number.
    elif i < smallest:
        smallest = i

# Print the result
print("Sum of even numbers is:", even_sum)
print("Sum of odd numbers is:", odd_sum)
print("Largest number in the list is:", largest)
print("Smallest number in the list is:", smallest)
