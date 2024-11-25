#Programmer: Matthew Washburn
#Program: Sales Display Weekly
#define main
def main():
    week = 1
    #create sales lists for each week
    sales = [ [300,534,345,632,654],
            [200,235,467,346,345],
            [300,500,235,645,346],
            [467,435,574,457,437] ]
    #calculate total sales
    for row in sales:
        total = 0
        for item in row:
            total += item
        sum = str(total)
        print(f"Week: {week} Total: {sum}")
        week += 1
    #call main
if __name__ == "__main__":
    main()

