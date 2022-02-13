# This is a program to calculate pay amount
# 1/30/2022
# Duong Vy (Ellie) Le

# Prompt user for number of hours worked
hours = input("Enter number of hours worked: ")

# Prompt user for hourly rate
rate = input("Enter hourly rate: ")

# Calculate the pay
pay_amount = float(hours) * float(rate)

# Print the pay amount
print("Your pay amount is:", pay_amount)
