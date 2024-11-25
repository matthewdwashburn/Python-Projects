#Programmer: Matthew Washburn
#Program: Character Counter in text file
try:
    #define character variables
    lowercase = 0
    uppercase = 0
    digits = 0
    whitespace = 0
    #ask for user file
    user_file = input("Enter the file name and extention: ")
    #create line loop
    infile = open(user_file, "r")
    data = infile.read()
    for char in data:
        if char.islower():
            lowercase += 1
        if char.isupper():
            uppercase += 1
        if char.isdigit():
            digits += 1
        if char.isspace():
            whitespace += 1
    infile.close()
    print(f"Lowercase Letters: {lowercase}")
    print(f"Uppercase Letters: {uppercase}")
    print(f"Digits: {digits}")
    print(f"Whitespaces: {lowercase}")
except FileNotFoundError:
    print("File not found. Please try again.")



