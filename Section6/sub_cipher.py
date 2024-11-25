#Programmer: Matthew Washburn
#Program: Encrypt Decrypt Message
def main():
    #get user message
    result = ""
    result2 = ""
    message = input("Enter a message:")
    for i in range(len(message)):
        char = message[i]
        result += chr(ord(char)+5)
    print (result)

    for i in range(len(result)):
        char = result[i]
        result2 += chr(ord(char)-5)
    print(result2)
main()