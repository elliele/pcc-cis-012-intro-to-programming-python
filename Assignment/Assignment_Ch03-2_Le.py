# This program will sort numbers in ascending order.
# 2/3/2022
# Duong Vy (Ellie)

# Prompts the user to input three numbers.
a = input("Please enter the first integer: ")
b = input("Please enter the second integer: ")
c = input("Please enter the third integer: ")

# Check conditions statement and print integer numbers in ascending order

if a < b and a < c and b < c:
    print("Input three integer numbers in ascending order: \n"+ a, b, c)
    
elif a < b and a < c and b > c:
    print("Input three integer numbers in ascending order: \n"+ a, c, b)
    
elif a > b and a < c and b < c:
    print("Input three integer numbers in ascending order: \n"+ b, a, c)
    
elif a < b and a > c and b > c:
    print("Input three integer numbers in ascending order: \n"+ c, a, b)
    
elif a > b and a > c and b > c:
    print("Input three integer numbers in ascending order: \n"+ c, b, a)
    
elif a > b and a > b and b < c:
    print("Input three integer numbers in ascending order: \n"+ b, c, a)
    
elif a > b and b == c:
    print("Input three integer numbers in ascending order: \n"+ b, c, a)
    
elif a == b and b < c:
    print("Input three integer numbers in ascending order: \n"+ a, b, c)
    
elif a < b and a == c:
    print("Input three integer numbers in ascending order: \n"+ a, c, b)
    
elif a > b and a == c:
    print("Input three integer numbers in ascending order: \n"+ b, a, c)

elif a == b and b == c:
    print("Input three integer numbers in ascending order: \n"+ a, b, c)
    
