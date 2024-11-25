#Programmer: Matthew Washburn
#Program: Head Display
#define main program
def main():
#user inputs file
    file = input("Enter a file name: ")
#call read fuction
    read(file)
#define read function
def read(f):
#specify reading parameters
    user_file = open(f, 'r')
    line = user_file.readline()
    line = line.rstrip('\n')
    count = 0
#while line count is 4 or less, execute read function
    while count <= 4:
        if line == '' :
            count += 5
        else:
            print(line)
            line = user_file.readline()
            line = line.rstrip('\n')
            count += 1
#close user file
    user_file.close()
#call main function
if __name__ == "__main__":
    main()