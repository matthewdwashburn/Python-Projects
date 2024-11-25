#Programmer: Matthew Washburn
#Program: Long Distance Call Rates
import tkinter
import tkinter.messagebox
class Phone:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()
        # create title
        self.main_window.title("Long-Distance Phone Call Calculator")
        # create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        #create texbox for result
        self.cost_calculation = tkinter.StringVar()
        self.rate_label = tkinter.Label(self.top_frame, textvariable=self.cost_calculation)
        #create explanation label
        self.title_label = tkinter.Label(self.bottom_frame, text="Long-Distance Rates")
        #create user minutes entry label
        self.minutes_entry = tkinter.Entry(self.bottom_frame, width=10, relief="groove", borderwidth=5)
        self.minutes_label = tkinter.Label(self.bottom_frame, text= "Enter Number of Call Minutes: ")
        #create calculate button in bottom frame
        self.calculate_button = tkinter.Button(self.bottom_frame, text="Total Charge", command=self.calculate_cost,
                                               relief="raised", borderwidth=2)
        #create radio buttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        #place radio buttons and set their int values
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Daytime (6:00 am – 5:59 pm) $0.10',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Evening (6:00 pm – 11:59 pm) $0.15',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Off-peak (midnight – 5:59 am) $0.05',
                                       variable=self.radio_var,
                                       value=3)
        #create quit button
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        #pack everything
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.rate_label.pack()
        self.title_label.pack()
        self.minutes_label.pack()
        self.minutes_entry.pack()
        self.calculate_button.pack()
        self.quit_button.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        tkinter.mainloop()
        #create calculation function
    def calculate_cost(self):
        self.minutes = float(self.minutes_entry.get())

        if self.radio_var.get() == 1:
            self.rate = 0.10
        if self.radio_var.get() == 2:
            self.rate = 0.15
        if self.radio_var.get() == 3:
            self.rate = 0.05
        self.charges = self.minutes * self.rate

        tkinter.messagebox.showinfo('Total charges',
                                    f'Total Charge: ${self.charges:,.2f}')
if __name__ == "__main__":
    calculate_cost = Phone()