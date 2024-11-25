#Programmer: Matthew Washburn
#Program: Favorite Movies
def main():
#Get movie input from user
    movie1 = input("What is your favorite movie?")
    movie2 = input("What is your 2nd favorite movie?")
    movie3 = input("What is your 3rd favorite movie?")
    movie4 = input("What is your 4th favorite movie?")
#open movies file
    movie_file = open("movies.txt", "a")
#write user input into moives file
    movie_file.write(movie1 + "\n")
    movie_file.write(movie2 + "\n")
    movie_file.write(movie3 + "\n")
    movie_file.write(movie4 + "\n")
#close movies file
    movie_file.close()
    infile = open("movies.txt", "r")
#display file with user input
    file_contents = infile.read()
    print(file_contents)
if __name__ == "__main__":
    main()