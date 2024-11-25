#Programmer:Matthew Washburn
#Date: February 6th 2022
#define main
def main():
#ask user for the actual value of the property
    property_value = float(input("Enter the property's actual value: "))
    prop_value(property_value)

def prop_value(property_value):
#calculate property assessment value
    assessment_value = property_value * 0.6
    print(f"The assessment value is: ${assessment_value:,.2f}")
    assessment(assessment_value)

def assessment(assessment_value):
#calculate the property tax.
    property_tax = assessment_value * 0.0072
    print(f"The property tax is: ${property_tax:,.2f}")

#call main function
main()
