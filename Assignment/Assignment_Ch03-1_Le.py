# This program calculates pay rate based on hours worked and hourly rate.
# 2/3/2022
# Duong Vy (Ellie) Le

# Prompts user for number of hours worked
try:
    hours = float(input("Enter number of hours worked for this week: "))
    if hours >=0:
        try:
            # Prompts user for the hourly rate
            hourly_rate = float(input("What is the hourly rate? "))
            if hourly_rate >= 0:
                if hours >0 and hours <= 40:
                    pay_amount= hourly_rate*hours
                    print("Your pay for this week is:", pay_amount)

                # If number of hours worked greater than 40 and less than and equal to 60
                # multiply hourly_rate by 1.5
                elif hours > 40 and hours <= 60:
                    pay_amount= hourly_rate*1.5*hours
                    print("Your pay for this week is:", pay_amount)

                # If number of hours worked greater than 60, multiply hourly_rate by 2.
                elif hours > 60:
                    pay_amount = hourly_rate*2*hours
                    print("Your pay for this week is:", pay_amount)

            else:
                print("You enter wrong information for hourly rate.")

    # If user enters wrong input, display message for wrong input
        except:
            print("You enter wrong information for hourly rate.")
            
    else:
        print("You enter wrong information for hours.")
        
        
except:
    print("You enter wrong information for hours.")
    

    
