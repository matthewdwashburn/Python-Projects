#Programmer: Matthew Washburn
#Program: Word Frequency in text file
from collections import Counter
def main():
    try:
        #get user text file
        user_file = input('Enter the name and extension of a file: ')
        #create file dictionary
        file_dictionary = {}
        #set variable to counter
        count = Counter()
        #read file
        infile = open(user_file, "r")
        #count words in file
        for line in infile:
            for word in line.split():
                count[word] += 1
                file_dictionary[word] = count[word]
        print(file_dictionary)
        #catch file not found error
    except FileNotFoundError:
        print("File not found please try again.")
        #call main function
if __name__ == "__main__":
    main()


