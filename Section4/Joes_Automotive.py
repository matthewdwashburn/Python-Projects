#Programmer: Matthew Washburn
#Program: Joe's Automotive

import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        # create title
        self.main_window.title("Joe's Automotive")
        # Create two frames. One for the checkbuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create three IntVar objects to use with
        # the Checkbuttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        # Create the Checkbutton widgets in the top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Oil Change - $30.00',
                                       variable=self.cb_var1, onvalue=30, offvalue=0)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Lude Job - $20.00',
                                       variable=self.cb_var2, onvalue=20, offvalue=0)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Radiator Flush - $40.00',
                                       variable=self.cb_var3, onvalue=40, offvalue=0)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text='Transmission Flush - $100.000',
                                       variable=self.cb_var4, onvalue=100, offvalue=0)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text='Inspection - $35.00',
                                       variable=self.cb_var5, onvalue=35, offvalue=0)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                       text='Muffler Replacement - $200.00',
                                       variable=self.cb_var6, onvalue=200, offvalue=0)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                       text='Tire Rotation - $20.00',
                                       variable=self.cb_var7, onvalue=20, offvalue=0)

        # Pack the Checkbuttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Create an OK button and a Quit button.
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.charge = tkinter.Button(self.bottom_frame, text="Total Charge", command=self.calculate_cost,
                                               relief="raised", borderwidth=2)

        # Pack the Buttons.
        self.charge.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the
    # OK button.
    
    def calculate_cost(self):
        # Create a message string.
        self.message = (self.cb_var1.get() + self.cb_var2.get() + self.cb_var3.get() + self.cb_var4.get() + self.cb_var5.get() + self.cb_var6.get() + self.cb_var7.get())
        # Display the message in an info dialog box.
        tkinter.messagebox.showinfo('Total charges', f'Total Charge: ${self.message:,.2f}')

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    calculate_cost = MyGUI()