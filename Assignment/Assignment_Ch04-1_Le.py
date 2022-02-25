# Created by Ellie Le at 2/9/2022
# This program used a function to calculate pay rate based on hours worked and hourly rate.


#Create a function called CalPay which take hrs and rate as argument
def CalPay (hrs, rate):
    if hrs > 0 and hrs <= 40:
        pay_amount = rate * hrs
        print("Your pay for this week is:", pay_amount)

    # If number of hours worked greater than 40 and less than and equal to 60 multiply hourly_rate by 1.5
    elif hrs > 40 and hrs <= 60:
        pay_amount = rate*1.5*(hrs-40) + rate*40
        print("Your pay for this week is:", pay_amount)

    # If number of hours worked greater than 60, multiply hourly_rate by 2.
    elif hrs > 60:
        pay_amount = rate*2*(hrs-60) + rate*1.5*20 + rate*40
        print("Your pay for this week is:", pay_amount)


# Prompts user for number of hours worked
try:
    hrs = float(input("Enter number of hours worked for this week: "))
    if hrs >= 0:
        try:
            # Prompts user for the hourly rate
            rate = float(input("What is the hourly rate? "))
            if rate >= 0:
                CalPay(hrs,rate)
            else:
                print("You enter wrong information for hourly rate.")

        # If user enters wrong input, display message for wrong input
        except:
            print("You enter wrong information for hourly rate.")

    else:
        print("You enter wrong information for hours.")


except:
    print("You enter wrong information for hours.")



