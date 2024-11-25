from tkinter import *
from tkinter import ttk
#Programmer: Matthew Washburn

ws = Tk()
ws.title('Student Table')
ws.geometry('800x450')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

# scrollbars
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

# Create table frame
my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column

my_game['columns'] = ('student_id', 'first_name', 'last_name', 'GPA')

# Format columns
my_game.column("#0", width=0, stretch=NO)
my_game.column("student_id", anchor=CENTER, width=80)
my_game.column("first_name", anchor=CENTER, width=80)
my_game.column("last_name", anchor=CENTER, width=80)
my_game.column("GPA", anchor=CENTER, width=80)

# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("student_id", text="Student ID", anchor=CENTER)
my_game.heading("first_name", text="First Name", anchor=CENTER)
my_game.heading("last_name", text="Last Name", anchor=CENTER)
my_game.heading("GPA", text="GPA", anchor=CENTER)

# Insert teams
my_game.insert(parent='', index='end', iid=0, text='',
               values=('1', 'John', 'Washburn','3.5'))
my_game.insert(parent='', index='end', iid=1, text='',
               values=('2', 'Jake', 'Washburn','3.6'))
my_game.insert(parent='', index='end', iid=2, text='',
               values=('3', 'Sam', 'Bureau','3.9'))
my_game.insert(parent='', index='end', iid=3, text='',
               values=('4', 'Elena', 'Frost','4.1'))
my_game.insert(parent='', index='end', iid=4, text='',
               values=('5', 'Rachel', 'Washburn','3.5'))
my_game.insert(parent='', index='end', iid=5, text='',
               values=('6', 'Angie', 'Washburn','3.8'))
my_game.insert(parent='', index='end', iid=6, text='',
               values=('7', 'Josh', 'Washburn','3.7'))
my_game.insert(parent='', index='end', iid=7, text='',
               values=('8', 'Terry', 'Morlan','3.3'))
my_game.insert(parent='', index='end', iid=8, text='',
               values=('9', 'Bethany', 'Witzke','3.2'))
my_game.insert(parent='', index='end', iid=9, text='',
               values=('10', 'Emma', 'Morlan','4.2'))
my_game.insert(parent='', index='end', iid=10, text='',
               values=('11', 'Justin', 'Bowser','3.3'))
my_game.pack()

frame = Frame(ws)
frame.pack(pady=20)

# Labels
playerid = Label(frame, text="ID")
playerid.grid(row=0, column=0)

playername = Label(frame, text="First Name")
playername.grid(row=0, column=1)

playerrank = Label(frame, text="Last Name")
playerrank.grid(row=0, column=2)

GPA = Label(frame, text="GPA")
GPA.grid(row=0, column=3)

# Entry boxes: ID, Name, Rank
playerid_entry = Entry(frame)
playerid_entry.grid(row=1, column=0)

playername_entry = Entry(frame)
playername_entry.grid(row=1, column=1)

playerrank_entry = Entry(frame)
playerrank_entry.grid(row=1, column=2)

GPA_entry = Entry(frame)
GPA_entry.grid(row=1, column=3)


# Select Record
def select_record():
    # clear entry boxes
    playerid_entry.delete(0, END)
    playername_entry.delete(0, END)
    playerrank_entry.delete(0, END)
    GPA_entry.delete(0,END)

    # Get row that has focus
    selected = my_game.focus()
    # grab record values
    values = my_game.item(selected, 'values')
    # temp_label.config(text=selected)

    # Insert focus row in entry boxes
    playerid_entry.insert(0, values[0])
    playername_entry.insert(0, values[1])
    playerrank_entry.insert(0, values[2])
    GPA_entry.insert(0, values[3])


# Update Record
def update_record():
    selected = my_game.focus()
    # save new data
    my_game.item(selected, text="", values=(playerid_entry.get(), playername_entry.get(), playerrank_entry.get(), GPA_entry.get()))

    # clear entry boxes
    playerid_entry.delete(0, END)
    playername_entry.delete(0, END)
    playerrank_entry.delete(0, END)
    GPA_entry.delete(0, END)


# Buttons
select_button = Button(ws, text="Select Record", command=select_record)
select_button.pack(pady=10)

refresh_button = Button(ws, text="Refresh Record", command=update_record)
refresh_button.pack(pady=10)

temp_label = Label(ws, text="")
temp_label.pack()

ws.mainloop()