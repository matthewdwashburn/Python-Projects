#Programmer: Matthew Washburn
#Program: Average of Numbers
def main():
    try:
            file = input("Enter file name with extenstion: ")
            numbers_file = open(file, 'r')
            number_count = 0
            total = 0
            for i in numbers_file:
                total += int(i)
                number_count += 1
            print(total / number_count)
            numbers_file.close()
    except IOError:
        print("An error occured trying to read the file.")

    except ValueError:
        print("Non-numeric data found in the file.")

    except:
        print("An error occured.")
if __name__ == "__main__":
    main()
