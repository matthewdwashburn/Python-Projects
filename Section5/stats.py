#Programmer: Matthew Washburn
#Program: Calculating Statistics
import statistics
def main():
    scores = [100, 94, 67, 78, 89, 54, 95, 83, 75, 62]
    average = statistics.mean(scores)
    minimum = str(min(scores))
    maximum = str(max(scores))
    print(f"The average of the scores was: {average}")
    print(f"The minimum of the scores was: {minimum}")
    print(f"The average of the scores was: {maximum}")
if __name__ == "__main__":
    main()
