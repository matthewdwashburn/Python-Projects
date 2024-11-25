#Name: Matthew Washburn
#Date: January 23rd
#attendance and hotdogs per person - user input
attendance = float(input("How many people are attending your cookout?"))
hotdogsperperson = float(input("How many hot dogs per person?"))
#Hot dog and bun packs calculations
HOT_DOGS_PER_PACKAGE = 10
HOT_DOG_BUNS_PER_PACKAGE = 8
totalhotdogs = attendance * hotdogsperperson
dogpackagesneeded = totalhotdogs / HOT_DOGS_PER_PACKAGE
bunpackagesneeded = totalhotdogs / HOT_DOG_BUNS_PER_PACKAGE
hotdogsleftover = totalhotdogs % HOT_DOGS_PER_PACKAGE
bunsleftover = totalhotdogs % HOT_DOG_BUNS_PER_PACKAGE
#display packs with remainders
print(f"You will need a minimum of {int(dogpackagesneeded)} hot dog packages, and {int(bunpackagesneeded)} hot dog bun packages for your cookout.")
print(f"You will have {int(hotdogsleftover)} hot dogs left over, and {int(bunsleftover)} hot dog buns left over.")