#Name: Matthew Washburn
#Date: January 23rd
#year user input
year = int(input("Enter a year:"))
#variable identification
february_days = 28
#february day calculation
if year % 100 == 0 and year % 400 == 0:
    print(f"In {year} February has {february_days + 1} days.")
elif year % 100 != 0 and year % 4 == 0:
    print(f"In {year} February has {february_days + 1} days.")
else:
    print(f"In {year} February has {february_days} days.")
