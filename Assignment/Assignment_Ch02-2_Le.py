# This is a program to convert seconds to hours, minutes, and seconds
# 1/30/2022
# Duong Vy (Ellie) Le

# Prompt user for elapsed time in seconds
event_time = input("Enter the elapsed time in seconds: ")

# Print the elapsed time in seconds
print("The elapsed time in seconds =" , event_time)

# Convert time_in_sec to hours, minutes, and seconds
# Concert time from string to integer
time_in_sec = int(event_time)

# Calculate hour by dividing the seconds by 3,600
hour = time_in_sec//3600

#Calculate minutes by getting the remainder of total time divide by 3600,
# then divide by 60
minutes = (time_in_sec %3600)//60


# Calculate seconds by get the remainder of total time divide by 60
seconds = time_in_sec %60

# Print time in hours, minutes, seconds
print("The equivalent time in hours:minutes:seconds = " + str(hour)+':'+str(minutes)+':'+str(seconds))
