#Programmer: Matthew Washburn
#Date: January 19 2021
#Input scores
score1 = float(input("What was your first test score?"))
score2 = float(input("What was your second test score?"))
score3 = float(input("What was your third test score?"))
average = (score1 + score2 + score3) / 3
#Display scores
print(f"Your average score is: {average:.2f}.")
#Print grade
if average >= 90:
    print("Grade = A")
else:

    if average >= 80:
        print("Grade = B")
    else:

        if average >= 70:
            print("Grade = C")
        else:

         if average >= 60:
            print("Grade = D")
         else:

            if average >= 50:
                print("Grade = F")
            else:
                if average < 50:
                    print("Grade = F")


