# Problem 10: WAP to accept a number from 1 to 7 and display the name of the day.
day = int(input("Enter a number (1-7): "))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if 1 <= day <= 7:
    print("Day is:", days[day-1])
else:
    print("Invalid input")