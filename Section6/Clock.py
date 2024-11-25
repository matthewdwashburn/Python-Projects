#Programmer: Matthew Washburn
#Date: January 28th
import time
hours = int(input("How many hours do you want the clock to run?"))
for hour in range(0, hours + 1):
    for min in range(0, 60):
        for sec in range(0, 60):
            print(f"\r Hours:"f"{hour} " + "Minutes:"f"{min} " + f"Seconds:"f"{sec}", end="")
            time.sleep(1)


