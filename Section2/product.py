#Programmer: Matthew Washburn
#Date: February 4th 2022
#define main function
def main():
    number1 = int(input("What is the first integer you would like to multipy?"))
    number2 = int(input("What is the second integer you would like to multipy?"))
    calculate(number1, number2)
#define calcuate function and print result
def calculate(num1, num2):
    result = num1 * num2
    print(f"The product is: {result:,}")
#call the main function
main()