#Programmer: Matthew Washburn
#Date: February 9th
#define main function
def main():
    infile = open("titles.txt", "r")
    file_contents = infile.read()
    infile.close()
#display text file
    print(file_contents)
if __name__ == "__main__":
#call main function
    main()
