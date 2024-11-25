#Programmer: Matthew Washburn
#Date: February 28th, 2022
def main():
    #ask for state
    how_many = int(input("How many states would you like to know the capital of?"))
    for r in range(how_many):
        user_state = str(input("Enter the name of a state: "))
        states_capitals = [ ["Iowa", "Kansas", "Minnesota", "Missouri", "Nebraska", "North Dakota", "South Dakota", "Wisconsin"],
                            ["Des Moines", "Topeka", "St Paul", "Jefferson City", "Lincoln", "Bismarck", "Pierre", "Madison"]]
        if user_state == (states_capitals[0][0]):
            print(f"This state's capital is {states_capitals[1][0]}.")
        if user_state == (states_capitals[0][1]):
            print(f"This state's capital is {states_capitals[1][1]}.")
        if user_state == (states_capitals[0][2]):
            print(f"This state's capital is {states_capitals[1][2]}.")
        if user_state == (states_capitals[0][3]):
            print(f"This state's capital is {states_capitals[1][3]}.")
        if user_state == (states_capitals[0][4]):
            print(f"This state's capital is {states_capitals[1][4]}.")
        if user_state == (states_capitals[0][5]):
            print(f"This state's capital is {states_capitals[1][5]}.")
        if user_state == (states_capitals[0][6]):
            print(f"This state's capital is {states_capitals[1][6]}.")
        if user_state == (states_capitals[0][7]):
            print(f"This state's capital is {states_capitals[1][7]}.")

if __name__ == "__main__":
    main()