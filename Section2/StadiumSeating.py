#Programmer: Matthew Washburn
#Date: Feburary 6th 2022
#ask user for number of tickets sold
def main():
    a_tickets = int(input("Enter number of class A tickets sold: "))
    b_tickets = int(input("Enter number of class B tickets sold: "))
    c_tickets = int(input("Enter number of class C tickets sold: "))
    income_generated(a_tickets, b_tickets, c_tickets)
#Display income from each ticket class
def income_generated(a, b, c):
    aincome = a * 20
    print(f"You generated ${aincome:,.2f} in sales from class A tickets.")
    bincome = b * 15
    print(f"You generated ${bincome:,.2f} in sales from class B tickets.")
    cincome = c * 10
    print(f"You generated ${cincome:,.2f} in sales from class C tickets.")
#call main function
main()
