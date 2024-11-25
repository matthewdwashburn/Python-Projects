#Programmer: Matthew Washburn
#Program: Initals
def main():
    #get user name
    name = input("Enter your first, middle, and last name.")
#split string into words
    initals = name.split()
#specify initals parameters
    for string in initals:
        print(string[0].upper(), sep="", end="")
        print(".", sep = " ", end = "")
main()