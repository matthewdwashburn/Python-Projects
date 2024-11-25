#Programmer: Matthew Washburn
#Program: Phone Number Letter Interpreter
def main():
    #Get user number
    user_number = list(input("Enter the area code in numeric form, then the prefix and phone number in letters (No Dashes): ").upper())
    #create list for converting letters to numbers
    new_number = []
    #identify numbers with letters
    for char in user_number:
        if char.isalpha():
            if char == "A" or char == "B" or char == "C":
                new_number.append(2)
            if char == "D" or char == "E" or char == "F":
                new_number.append(3)
            if char == "G" or char == "H" or char == "I":
                new_number.append(4)
            if char == "J" or char == "K" or char == "L":
                new_number.append(5)
            if char == "M" or char == "N" or char == "O":
                new_number.append(6)
            if char == "P" or char == "Q" or char == "R" or char == "S":
                new_number.append(7)
            if char == "T" or char == "U" or char == "V":
                new_number.append(8)
            if char == "W" or char == "X" or char == "Y" or char == "Z":
                new_number.append(9)
    #join number list together as a string
    newtotal = "".join(map(str, new_number))
    #join area code together as a string
    area_join = "".join(map(str, user_number[0:3]))
    #catch if area code is a letter
    if user_number[0].isalpha() or user_number[1].isalpha() or user_number[2].isalpha():
        print("The area code was inputted as a letter. Please try again.")
    #print number
    else:
        print(area_join + newtotal)
main()

