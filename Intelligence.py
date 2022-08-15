Year = input("Enter the year to be checked : ")

if(Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0):
    print("This year is a Leap Year")
else:
    print("This year is't a Leap Year")