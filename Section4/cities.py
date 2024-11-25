#Programmer: Matthew Washburn
#Program: Cities
def main():
    #define citites and latitudes
    cities = { "Nairobi" : 1, "Johannesburg" : 26, "Cairo" : 30, "Abidjan" : 5, "Khartoum" : 15, "Zanzibar" : 6 }
    #define tropic cities
    tropic_cities = { k:v for k,v in cities.items() if v <= 23 }
    #display tropic cities
    print("These are the cities in the tropic of cancer or the tropic of capricorn:")
    for key in tropic_cities:
        print(key)
if __name__ == "__main__":
    main()