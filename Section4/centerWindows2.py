from tkinter import *
#Programmer: Matthew Washburn
def center_window(w=1500,h=1500):
    # get screen width and height
    ws = main_window.winfo_screenwidth()
    hs = main_window.winfo_screenheight()

    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    main_window.geometry('+%d+%d' %  (x,y))

main_window = Tk()
center_window(200,250)
main_window.mainloop()


