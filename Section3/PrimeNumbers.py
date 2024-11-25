#Programmer: Matthew Washburn
#Date: February 9th
#define main function
def main():
    number = int(input("Enter a number: "))
#call prime identifier
    is_prime(number)
    prime = is_prime(number)
#display prime result
    if prime == True:
        print(f"{number} is a prime number.")
    if prime == False:
        print(f"{number} is not a prime number.")
#define prime identifier
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                prime = False
            elif (n % i) != 0:
                prime = True
            break
    return prime
#call main function
main()