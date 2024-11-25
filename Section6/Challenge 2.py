#Programmer: Matthew Washburn
#Date: February 28th, 2022
def main():
    try:

        user_seconds = float(input("Enter number of seconds: "))
        hours = float(user_seconds / 3600)
        minutes = float(user_seconds / 60)
        seconds = user_seconds
        print(f"That amount of time {hours} hours, {minutes} minutes, or {seconds} seconds.")
    except ValueError:
        print("Non numeric value inputted. Please inpute a numeric value.")

if __name__ == "__main__":
    main()
