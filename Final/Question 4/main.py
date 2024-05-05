#glasses class
class Glasses:
    #constructor
    def __init__(self, color, price, perscription):
        #self.color = color
        self.__price = price
        self.__perscription = perscription
    #set price
    def set_price(self, price):
        self.__price = price
    
    #set perscription
    def set_perscription(self, perscription):
        self.__perscription = perscription
    
    #get price
    def get_price(self):
        return self.__price

    #get perscription
    def get_perscription(self):
        return self.__perscription
    
    #to string
    def __str__(self):
        return "The glasses's perscription is " + str(self.__perscription) + " and the price is " + str(self.__price) + "."

#bifocals class
class Bifocals(Glasses):
    #constructor
    def __init__(self, color, price, perscription, reading_perscription):
        super().__init__(color, price, perscription)
        self.__reading_perscription = reading_perscription
    
    #set reading perscription
    def set_reading_perscription(self, reading_perscription):
        self.__reading_perscription = reading_perscription

    #get reading perscription
    def get_reading_perscription(self):
        return self.__reading_perscription
    
    #to string
    def __str__(self):
        return super().__str__() + " The reading perscription for these bifoals is " + str(self.__reading_perscription) + "."

#main function
def main():
    #create glasses object
    glasses = Glasses("black", 150, 2.5)

    #set price
    glasses.set_price(200)

    #set perscription
    glasses.set_perscription(3.5)

    #print price and perscription
    print(str(glasses.get_price()) + " " + str(glasses.get_perscription()))

    #test to string
    print(glasses)

    #create bifocals object
    bifocals = Bifocals("blue", 200, 4, 3)

    #set reading perscription
    bifocals.set_reading_perscription(2)

    #print reading perscription
    print(bifocals.get_reading_perscription())

    #test to string
    print(bifocals)

#run main
if __name__ == "__main__":
    main()