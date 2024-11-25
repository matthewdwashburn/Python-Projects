#Programmer: Matthew Washburn
#Program: Baby Name Search
#get user boy baby name
def main():
    user_boy = input("Enter a boy baby name: ")
    #read file and set found as false unless found
    boy_names = open("BoyNames.txt", "r")
    foundboy = False
    #search boy file and display result
    for line in boy_names:
        if user_boy in line:
            foundboy = True
    if foundboy == True:
        print("This name is in the top 200 baby names for boys.")
    if foundboy == False:
        print("This name is not in the top 200 baby names for boys.")
    #repeat process for girls
    user_girl = input("Enter a girl baby name: ")
    girl_names = open("GirlNames.txt", "r")
    foundgirl = False
    for line in girl_names:
        if user_girl in line:
            foundgirl = True
    if foundgirl == True:
        print("This name is in the top 200 baby names for girls.")
    if foundgirl == False:
        print("This name is not in the top 200 baby names for girls.")
#call main function
main()