#Programmer: Matthew Washburn
#Program: Course Information
def main():
    #get user course code
    course_code = input("Enter the course code: ")
    #create course dictionary
    course_dictionary = {'CS101': 'Room Number: 3004 | Instructor: Haynes | Meeting Time: 8:00 a.m.',
                         'CS102': 'Room Number: 4501 | Instructor: Alvarado | Meeting Time: 9:00 a.m.',
                         'CS103': 'Room Number: 6755 | Instructor: Rich | Meeting Time: 10:00 a.m.',
                         'NT110': 'Room Number: 1244 | Instructor: Burke | Meeting Time: 11:00 a.m.',
                         'CM241': 'Room Number: 1411 | Instructor: Lee | Meeting Time: 1:00 p.m.'}
    #search for course code in dictionary and display results to user
    if course_code in course_dictionary.keys():
        print(course_dictionary[course_code])
    else:
        print("Course code not found. Please Try again.")
if __name__ == "__main__":
    main()