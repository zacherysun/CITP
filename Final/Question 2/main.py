#main function
def main():
    #string
    greeting = "  Hello, little people of Earth!      "

    #print length of string
    print(len(greeting))

    #check if divisible by 5
    if len(greeting) % 5 == 0:
        print("The length of the string is divisible by 5")
    else:
        print("The length of the string is not divisible by 5")
    
    #Remove spaces at beginning and end of string
    newGreeting = greeting.strip()

    print(newGreeting)

    #store first 5 characters of string
    firstFive = newGreeting[:5]
    print(firstFive)

    #print out new string with 59 o
    print(firstFive + "o" * 59)


#run main function
if __name__ == "__main__":
    main()