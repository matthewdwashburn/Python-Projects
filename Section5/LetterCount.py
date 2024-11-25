#Programmer: Matthew Washburn
#Program: Letter Count
#get name from user
def main():
    name = str(input("Enter your full name: "))
    count = 0
    #search for letter a
    for char in name:
        if char == "a" or char == "A":
            count += 1
    #display letter a count
    if count == 1:
        print(f"The letter a appears {count} time in your name.")
    else:
        print(f"The letter a appears {count} times in your name.")
    #call main
if __name__ == "__main__":
    main()


