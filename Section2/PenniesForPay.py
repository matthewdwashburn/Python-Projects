#Programmer:Matthew Washburn
#Date:January 26th
#user inputs days
days = int(input("Input number of days:"))
#penny doubling calcuation
total_pennies = 0
for day in range(days):
    pay = 2 ** day
    total_pennies += pay
    print(day+1, '\t', pay)
total_pay = total_pennies / 100
#display total pay
print(f"The total pay was: ${float(total_pay):,.2f}")