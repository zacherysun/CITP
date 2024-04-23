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
        self.button = tkinter.Button(self.main_window, text="Convert to Fahrenheit", command=self.convert)
        self.button.pack()

        #label for output
        self.output = tkinter.Label(self.main_window, text="")
        self.output.pack()

        #Start the main loop
        tkinter.mainloop()
    
    #convert function
    def convert(self):
        #convert celsius to fahrenheit
        f = (9/5) * float(self.celsius.get()) + 32
        #change the output label
        self.output.config(text=f"{f} degrees Fahrenheit")


#Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()