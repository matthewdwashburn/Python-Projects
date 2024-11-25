#Programmer: Matthew Washburn
#Date: February 6th 2022
#import modules
import random
import operator
#ask user number of quiz questions
questions = int(input("Enter number of math quiz questions: "))
#define global operators
operators = {'+': operator.add,
               '-': operator.sub,
               '*': operator.mul,
               '/': operator.truediv}
#define quiz and display inputted number of questions
for quiz in range(questions):

    def main():
        num1 = random.randint(0, 1000)
        num2 = random.randint(1, 1000)
        operation = random.choice(list(operators.keys()))
        math_quiz(num1, num2, operation)
    def math_quiz(num1, num2, operation):
        score = 0
        math = operators.get(operation)(num1, num2)
        print(f"{num1} {operation} {num2}")
        user_answer = float(input("Compute the answer to the problem: "))
#display incorrect and correct responses to user
        if user_answer == math:
            print("Correct!")
        elif user_answer != math:
            print(f"Incorrect. The correct answer was {math}.")
        math_quiz.score = score
    main()



