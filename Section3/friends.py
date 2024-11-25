#Programmer: Matthew Washburn
#Program: Friend Lister
def main():
    friends = ["Sam", "Justin", "Elliot", "Eli", "Kavan"]
    index = 0
    while index < len(friends):
        print(friends[index])
        index += 1
    print()
    friends[1] = "Joe"
    friends[2] = "Mama"
    index = 0
    while index < len(friends):
        print(friends[index])
        index += 1
if __name__ == "__main__":
    main()



