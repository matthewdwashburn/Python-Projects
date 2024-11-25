#Programmer:Matthew Washburn
#Date: January 21st

#Create Constants
HIGH = 1.5
MEDIUM = 1.25
LOW = 1.0
#Get User Input
gender = (input("What is your gender? (M/F)"))
while gender != "M" or gender != "F":
    print("Invalid Entry")
    gender = (input("What is your gender? (M/F)"))
    if gender == "M" or gender == "F": break
age = int(input("What is your age?"))
#Determin Factor
if gender == "M" and age < 25:
    factor = HIGH
    print(f"Male and under age 25: factor = {factor}")
elif gender == "M" and age >= 25:
    factor = MEDIUM
    print(f"Male and over age 25: factor = {factor}")
elif gender == "F" and age < 25:
    factor = MEDIUM
    print(f"Female and under age 25: factor = {factor}")
elif gender == "F" and age > 25:
    factor = LOW
    print(f"Female and over age 25: factor = {factor}")


