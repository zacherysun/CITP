#imports
import tkinter

#gui class
class MyGUI:
    #Constructor
    def __init__(self):
        self.main_window = tkinter.Tk()

        #label for input
        self.label = tkinter.Label(self.main_window, text="Enter a temperature in Celsius")
        self.label.pack()

        #input box
        self.celsius = tkinter.Entry(self.main_window)
        self.celsius.pack()

        #button to convert
        self.button = tkinter.Button(self.main_window, text="Convert to Fahrenheit")
        self.button.pack()

        #Start the main loop
        tkinter.mainloop()

#Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()