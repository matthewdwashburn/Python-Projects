#Programmer: Matthew Washburn
#Program: Miles Per Gallon Calculator
import tkinter
import tkinter.messagebox
class MPG:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()
        #create title
        self.main_window.title("Miles Per Gallon Calculator")
        #create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        #create text variable for calculation result in top frame
        self.result = tkinter.StringVar()

        self.result_label = tkinter.Label(self.top_frame, textvariable=self.result)
        #create buttons
        self.calculate_button = tkinter.Button(self.bottom_frame, text="Calculate MPG", command=self.calculate_mpg,
                                               relief="raised", borderwidth=5)
        #create labels
        self.miles_label = tkinter.Label(self.bottom_frame, text="Enter Miles:")
        self.gallons_label = tkinter.Label(self.bottom_frame, text="Enter Gallons:")
        #create entry widgets
        self.miles_entry = tkinter.Entry(self.bottom_frame, width=10, relief="groove", borderwidth=5)
        self.gallons_entry = tkinter.Entry(self.bottom_frame, width=10, relief="groove", borderwidth=5)
        #pack bottom frame labels & widgets
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")
        self.gallons_label.pack(side="left")
        self.gallons_entry.pack(side="left")
        self.result_label.pack(side="top")
        #pack calculate button
        self.calculate_button.pack(side="bottom")
        #pack top and bottom frame
        self.top_frame.pack()
        self.bottom_frame.pack()
        #mainlopp tkinter
        tkinter.mainloop()
    def calculate_mpg(self):
        #get user value into a variable for miles and gallons
        miles = float(self.miles_entry.get())
        gallons = float(self.gallons_entry.get())
        #calculate mpg
        calculation_result = float(miles / gallons)
        #display calculation in top frame
        self.result.set(f"MPG: {float(calculation_result):,.2f}")
if __name__ == "__main__":
    calculate_mpg = MPG()





