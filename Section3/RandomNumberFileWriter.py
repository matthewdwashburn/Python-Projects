#Programmer: Matthew Washburn
#Program: Random Number File Writer
#import random module
import random
#get variables in main
def main():
    file = input("Enter name and extenion of file: ")
    nbr_of_randoms = int(input("How many numbers do you want in the file?"))
    infile = open(file, "w")
#print random numbers in user file
    for i in range(nbr_of_randoms):
        number = random.randrange(1,501)
        number = str(number)
        infile.write(number)
        infile.write("\n")
    infile.close()
if __name__ == "__main__":
#call main
    main()