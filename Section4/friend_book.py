#Programmer: Matthew Washburn
#Program: Friend Book Dictionaries
#define main function
def main():
#make inital friend book dictionary
    friend_book = { "Alyssa" : "St. Paul", "Ben" : "Bloomington", "Jake" : "Circle Pines", "John" : "New York", "Gary" : "Atlanta" }
#display friend book
    for key,value in friend_book.items():
        print(key, value)
    print()
#add 2 friends to dictionary
    friend_book["Sam"] = "Blaine"
    friend_book["Justin"] = "Andover"
#display friend book
    for key, value in friend_book.items():
        print(key, value)
    print()
#remove added friends to dictionary
    if "Justin" in friend_book:
        del friend_book["Justin"]
    if "Sam" in friend_book:
        del friend_book["Sam"]
#display friend book
    for key, value in friend_book.items():
        print(key,value)
    print()
if __name__ == "__main__":

    main()