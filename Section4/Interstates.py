#Programmer: Matthew Washburn
#Program: Interstates
def main():
    #define interstates dictionary
    interstates = { "MN":35, "SF":80, "SE":90, "WA":94, "MI":95, "TC":494 }
    #define east-west interstates
    east_west = {k:v for k,v in interstates.items() if v % 2 <= 0 }
    #display east-west interstates
    print(f"Routes that are East-West: {east_west}")
    #define important routes
    important_route = {k: v for k, v in interstates.items() if v % 5 <= 0 and v % 2 <= 0}
    #display important routes
    print(f"Routes that are important: {important_route}")
if __name__ == "__main__":
    main()
