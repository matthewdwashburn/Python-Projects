#Programmer: Matthew Washburn
#Date: February 7th
#define tax rate
TAX_RATE = 0.07
#get item prices from user
def main():
    first = float(input("What is the value of the first item?"))
    second = float(input("What is the value of the second item?"))
    third = float(input("What is the value of the third item?"))
    subtotal, sales_tax, final_price = tax(f=first, s=second,t=third)
    #display subtotal
    print(f"Your subtotal is: ${subtotal:,.2f}")
    #display sales tax
    print(f"Your sales tax is: ${sales_tax:,.2f}")
    #display final price
    print(f"Your total is: ${final_price:,.2f} after tax.")
def tax(f, s, t):
    subtotal = f + s + t
    sales_tax = subtotal * TAX_RATE
    final_price = subtotal + (subtotal * TAX_RATE)
    return subtotal, sales_tax, final_price
#call main function
main()