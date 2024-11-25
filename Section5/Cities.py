#Programmer: Matthew Washburn
#Program: City Lister
def main():
        cities = ["New York", "Chicago", "Minneapolis", "St. Paul", "Seattle"]
        not_go = input("Where would you not like to go?")
        try:
            cities_index = cities.index(not_go)
            new_city = input("That city was found. Where would you like to go instead?")
            cities[cities_index] = new_city
            print("Here is the new cities list: ")
            print(cities)
        except ValueError:
            print("City not found. See all cities in route below: ")
            print(cities)
if __name__ == "__main__":
    main()


