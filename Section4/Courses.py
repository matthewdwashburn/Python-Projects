import tkinter
import tkinter.messagebox
#Programmer: Matthew Washburn
class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.title("List Courses")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.value = tkinter.StringVar()

        self.course_label = tkinter.Label(self.top_frame, textvariable = self.value)

        self.course_button = tkinter.Button(self.bottom_frame, text="Show Courses", command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.course_button.pack()
        self.quit_button.pack()
        self.course_label.pack()

        self.course_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        self.value.set("Math\nEnglish\nScience")
if __name__ == "__main__":
    show_info = MyGUI()
