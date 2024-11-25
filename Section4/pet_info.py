#Programmer: Matthew Washburn
#Program: Pet Info
# Get pet data.
from pets_project import Pet
def main():
    pet_name = ""
    pet_type = ""
    pet_age = 0
    pet_name = input('Enter the name of the pet:' )
    pet_type = input('Enter the type of animal:' )
    pet_age = int(input('Enter the age of the pet:' ))

    #Create a pet instance
    mypet = Pet(name, pet_type, pet_age)

    print('Here is the data that you entered: ')
    print(f'Pet name: {mypet.get_name()}')
    print(f'Animal type: {mypet.get_animal_type()}')
    print(f'Age of pet: {mypet.get_age()}')
if __name__ == "__main__":
    main()