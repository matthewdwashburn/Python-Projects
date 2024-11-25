#Programmer: Matthew Washburn
#Program: Age
#ask user for age
def main():
    try:
        age = int(input("What is your age?"))
        if age == int:
#display age
            print(f"You are {age} years old.")
#trap exceptions
    except ValueError:
        print(f"Error: Age is not an integer. Please input an integer.")
#call main
if __name__ == "__main__":
    main()








