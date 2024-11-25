#Programmer: Matthew Washburn
#Date: January 23rd
#package weight user input
package_weight = float(input("How much does your package weigh in pounds?"))
#package rate calculations
package_rate1 = 1.5 * package_weight
package_rate2 = 3 * package_weight
package_rate3= 4 * package_weight
package_rate4 = 4.75 * package_weight
#display options based on package rate
if package_weight <= 2:
    print(f"Your package shipping cost is ${package_rate1:.2f}.")
elif package_weight > 2 and package_weight <=6:
    print(f"Your package shipping cost is ${package_rate2:.2f}.")
elif package_weight > 6 and package_weight <= 10:
    print(f"Your package shipping cost is ${package_rate3:.2f}.")
elif package_weight > 10:
    print(f"Your package shipping cost is ${package_rate4:.2f}.")
