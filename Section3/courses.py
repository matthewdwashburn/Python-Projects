#Programmer: Matthew Washburn
#Program: Courses
def main():
#list courses
    courses = ["MAT3223", "MAT3252", "MAT3335", "PHY1201",
               "PHY1202", "EGR1005", "EGR2105", "EGR2206", "EGR2207", "EGR3115"]
#ask user for course
    user_course = input("Enter a course title to search for: ")
#determine if user inputted code is present in the list
    if user_course in courses:
        print("This course is present in the list.")
    else:
        print(f"The course \"{user_course}\" cannot be found in the list")
if __name__ == "__main__":
    main()

