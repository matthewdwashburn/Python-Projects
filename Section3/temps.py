#Programmer: Matthew Washburn
#Program: Average Low Temperature
def main():
    temps = []
    for number in range(1,8):
        temp = float(input("Enter day " + str(number) + " low temp in degrees fahrenheit:"))
        temps.append(temp)
    total = sum(temps)
    average = total/number
    print(f"The average low temperature last week was {average} degrees fahrenheit.")
if __name__ == "__main__":
    main()



