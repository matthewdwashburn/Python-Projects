#Programmer: Matthew Washburn
#Program: Item Counter
#call line counter in main
def main():
    line_count()
#define line count function
def line_count():
#open file and read line by line
    user_file = open("names.txt", 'r')
    line = user_file.readline()
    line = line.rstrip('\n')
    count = 0
#while there there are still lines, increase item count by one and repeat
    while line != '':
        count += 1
        line = user_file.readline()
        line = line.rstrip('\n')
    user_file.close()
    print(f"There are {count} items in names.txt.")
#call main function
if __name__ == "__main__":
    main()


