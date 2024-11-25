#Programmer: Matthew Washburn
#Date: February 4th 2022
#define global variables
count = 0
#define main function
employee_number = int(input("How many employees do you have? "))
for employees in range(employee_number):
    def main():
        first = input("Enter employee first name: ")
        last = input("Enter employee last name: ")
        employee(first, last)
#define employee function
    def employee(name1, name2):
        global count
        count += 1

        print("Employee: " + name1 + " " + name2)
        print("Employee ID: " + str(count))
    __name__ == "__main__"
#call main function
    main()