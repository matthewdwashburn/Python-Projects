#Programmer: Matthew Washburn
#Date: February 9th
#define main function
def main():
#prompt user to enter account information
    current = float(input("Enter the current value of the account: "))
    interest = float(input("Enter the monthly interest rate: "))
    months = int(input("Enter the number of months the account will collect interest: "))
    final = future(c=current, i=interest, m=months)
    future(c=current, i=interest, m=months)
#display future account value to user
    print(f"The value of the account after {months} months is: ${final:,.2f}")
#define future account value calculation
def future(c, i, m):
    final = c * ((1 + i) ** m)
    return final
#call main function
main()