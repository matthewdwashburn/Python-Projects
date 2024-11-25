#Programmer: Matthew Washburn
#Date: January 26th
#User inputs years
years = int(input("Input the number of years:"))
rainfall_month = 0
#User inputs rainfall and calculates average
for years in range(1, years + 1):
    for months in range(1,13):
        rainfall_inches = float(input("Input the number of inches of rainfall for this month:"))
        rainfall_month += rainfall_inches
        average_rainfall = rainfall_month / months
#total months calculated
total_months = years * 12
#results displayed
print(f"The total number of months is {total_months}, the total amount of rainfall is {rainfall_month:.2f}"
      f" inches, and the average monthly rainfall is {average_rainfall:.2f} inches.")


