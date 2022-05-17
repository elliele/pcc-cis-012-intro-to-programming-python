# Created by Ellie Le at 2/14/2022

# This program calculates pay rate based on hours worked and hourly rate.
# If the program enters improper input, the program will ask user to provide proper inputs again.
# Then the program will ask if the user wants to repeat the calculation.

#Create a function called CalPay which take hrs and rate as argument
def CalPay (hrs, rate):
    if hrs > 0 and hrs <= 40:
        pay_amount = rate * hrs
        print(f"Your pay for this week is: ${pay_amount}")


    # If number of hours worked greater than 40 and less than and equal to 60 multiply hourly_rate by 1.5
    elif hrs > 40 and hrs <= 60:
        pay_amount = rate*1.5*(hrs-40) + rate*40
        print(f"Your pay for this week is: ${pay_amount}")

    # If number of hours worked greater than 60, multiply hourly_rate by 2.
    elif hrs > 60:
        pay_amount = rate*2*(hrs-60) + rate*1.5*20 + rate*40
        print(f"Your pay for this week is: ${pay_amount}")




# Use a while loop to ask the user for number of hrs if entered incorrectly
while True:

    # Prompts user for number of hours worked
    hrs = input("Enter number of hours worked for this week: ")
    if hrs.isnumeric():

        # Use a while loop to ask the user for rate if entered incorrectly
        while True:
            # Prompts user for the hourly rate
            rate = input("What is the hourly rate? ")
            if rate.isnumeric():
                hrs = float(hrs)
                rate = float (rate)
                CalPay(hrs,rate)

                # Ask if the user wants to repeat the calculation
                repeat = input("Do you want another pay calculation? (y or n) ")

                # if repeat == 'y', then ask for new hrs and rate
                if repeat == 'y':
                    break

                # if repeat == 'n', then break out of the first loop
                elif repeat == 'n':
                    break

            else:
                # If user enters wrong input, display message for wrong input
                print("You enter wrong information for hourly rate.")

        # if repeat == 'n', then break out of the second loop
        if repeat == 'n':
            print("Good Bye!")
            break

    else:
        # If user enters wrong input, display message for wrong input
        print("You enter wrong information for hours.")




