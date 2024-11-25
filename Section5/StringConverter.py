#Programmer: Matthew Washburn
#Program: String Converter
def main():
    #get variable
    result = " "
    #get user input
    user_string = str(input("Enter a string:"))
    result = result + user_string[0]
#create a loop for each character in the string
    for i in range(1, len(user_string)):

        char = user_string[i]
#convert uppers to lowers and add spaces
        if char.isupper():
            char = char.lower()
            result = result + " "
        result = result + char
    print(result)
main()




