#wow_kazow function
def wow_kazow(num):
    #check if number is disible by 5 and 7
    if num % 5 == 0 and num % 7 == 0:
        return "wowkazow"
    #check if only divisible by 5
    elif num % 5 == 0:
        return "wow"
    #check if only divisible by 7
    elif num % 7 == 0:
        return "kazow"
    #return num if not divisible by 5 or 7
    return num
    

#main function
def main():
    #loop through 41-89
    for i in range(41, 90):
        print(wow_kazow(i))

#run main
if __name__ == "__main__":
    main() 