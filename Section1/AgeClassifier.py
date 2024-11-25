#Programmer: Matthew Washburn
#Date: January 21st
#user age input
age = float(input("What is your age?"))
#age title identifier
if age <= 1:
    print("You are an infant.")
elif age > 1 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20:
    print("Your are an adult.")