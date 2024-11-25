#Programmer: Matthew Washburn
#Date: February 28th, 2022
def main():
    count = 1
    year_count = 2
    rate_increase = count * 0.03
    print("The tution is initally $20000 the first year.")
    for r in range(4):
        tuition = 20000 * (count * rate_increase) + 20000
        print(f"In year {year_count} the tuition will be ${tuition}.")
        count += 1
        year_count += 1
if __name__ == "__main__":
    main()
