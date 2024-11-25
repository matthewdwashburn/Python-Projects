#Programmer: Matthew Washburn
#Date: Feubrary 7th
def main():
    length = float(input("What is the length in meters of the box?"))
    width = float(input("What is the width in meters of the box?"))
    height = float(input("What is the height in meters of the box?"))
    final = volume(l=length, w=width, h=height)
    volume(l=length, w=width, h=height)
    print(f"The volume of the box is: {final:,.2f} cubic meters")
def volume(l, w, h):
    final = l * w * h
    return final
main()
