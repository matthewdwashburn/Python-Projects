#Name: Matthew Washburn
#Date: January 26th
count = sum = avg = 0
print("Input Product Sale: (input 0 to stop entering sales)")

while True:
    amount = float(input("Sale amount:"))
    if amount == 0:
        break
    else:
        sum += amount
        count += 1
if count > 0:
    avg = (sum/count)
print(f"Total sales: "f"${sum:,.2f}")
print(f"Number of sales: {count}")
print(f"Average sales: ${avg:,.2f}")
