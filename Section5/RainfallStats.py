#Programmer: Matthew Washburn
#Program: Rainfall Stats
import statistics
def main():
    #get rainfall average from user
    count = 1
    rainfall = []
    for months in range(0,12):
        user_rain = float(input(f"Enter month {count} rainfall in inches:"))
        count += 1
        #compile user data into list
        rainfall.append(user_rain)
    #display rain data
    print(f"The total amount of rainfall for the year was {sum(rainfall)} inches. ")
    print(f"The average monthly rainfall for the year was {sum(rainfall)/12} inches. ")
    print(f"The highest amount of rainfall in a month was {max(rainfall)} inches.")
    print(f"The lowest amount of rainfall in a month was {min(rainfall)} inches.")
if __name__ == "__main__":
    main()
