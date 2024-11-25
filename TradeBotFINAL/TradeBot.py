import tkinter
from tkinter import *
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import alpaca_trade_api as api
import sqlite3
from tkinter import ttk
import time
import math
from alpaca_trade_api.rest import REST, TimeFrame
from datetime import timedelta
import threading
"""
Author: Matthew Washburn
"""
#set up window
root = Tk()
root.config(bg="#1A1A1B")
root.title("TradeBot")
#set window fullscreen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (screen_width, screen_height))
#connect portfolio equity database
conn = sqlite3.connect('portfolio_equity.db')
c = conn.cursor()

#alpaca connection
key = 'PK5OR2ARKBHAG674ZIHQ'
secret = '7vbYqdbw1NYrxjYuHuDDkVg0hHtct834sMKRZxKe'
alpaca_paper = 'https://paper-api.alpaca.markets'
api = api.REST(key_id=key, secret_key=secret, base_url=alpaca_paper, api_version='v2')
def login_page():
    #title label
    title = Label(root, text="TradeBot", font=("System", 40, "bold"),
                   fg="#02FF80", bg="#1A1A1B")
    #login labels
    user_label = Label(root, text="Username:", font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
    password_label = Label(root, text="Password:", font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
    #login entry boxes
    username_entry = Entry(root, width=20, borderwidth=1, highlightbackground='#AAAAAA', highlightthickness=1)
    password_entry = Entry(root, width=20, borderwidth=1, highlightbackground='#AAAAAA', highlightthickness=1, show="*")
    #show password button
    checkbox = IntVar(value=0)

    def show_password():
        if (checkbox.get() == 1):
            password_entry.config(show='')
        else:
            password_entry.config(show='*')

    username = "Matthew"
    password = "Washburn"

    show_button = tkinter.Checkbutton(fg="#808080", bg="#1A1A1B", variable=checkbox, onvalue=1, offvalue=0, command=show_password)
    #show password label
    show_label = Label(text='Show Password', font=("System", 12,), fg="#808080", bg="#1A1A1B")
    incorrect_label = Label(text="Incorrect username or password. Please try again.", font=("System", 12),
                            fg="red", bg="#1A1A1B")
    #login button
    def login():
        if (username_entry.get()) == username and (password_entry.get()) == password:
            portfolio_page()
        else:
            incorrect_label.place(relx=.5, rely=.515, anchor="center")

    login_button = Button(text="Login", font=("System", 15, "bold"), fg="black",
                          highlightbackground='#02FF80', height=1, width=4, command=login)


    #place everything
    title.place(relx=.5, rely=.325, anchor="center")
    user_label.place(relx=.375, rely=.397)
    password_label.place(relx=.377, rely=.447)
    username_entry.place(relx=.435, rely=.4)
    password_entry.place(relx=.435, rely=.45)
    show_button.place(relx=.57, rely=.452)
    show_label.place(relx=.586, rely=.452)
    login_button.place(relx=.5, rely=.56, anchor="center")
    def portfolio_page():
        #destroy login page
        title.destroy()
        user_label.destroy()
        password_label.destroy()
        username_entry.destroy()
        password_entry.destroy()
        show_button.destroy()
        show_label.destroy()
        login_button.destroy()
        incorrect_label.destroy()
        Top_Frame = Frame(root, width=1500, height=30, bg="#02FF80")
        Top_Frame.pack(side="top")
        portfolio_label = Label(root, text="TradeBot Portfolio", font=("System", 22, "bold"),
                   fg="#000000", bg="#02FF80")
        portfolio_label.place(relx=.5, rely=.018, anchor=CENTER)

        #call portfolio graph
        portfolio_graph()
        #update equity label
        def update_equity():
            account = api.get_account()
            equity = account.__getattr__('equity')
            equity_float = float(equity)
            equity_label.config(text=f"Equity: ${equity_float:,.2f}")
            root.after(1000, update_equity)
        #create top graph frame
        top_graph = Frame(root, height=75, width=675, highlightbackground='#AAAAAA', highlightthickness=3, bg="#1A1A1B")
        equity_label = Label(top_graph, text="", font=("System", 40, "bold"),
                                 fg="#02FF80", bg="#1A1A1B")
        top_graph.place(relx=.078, rely=.14)
        equity_label.place(relx=.24, rely=.07)
        update_equity()
        #create treeview
        top_history = Frame(root, height=75, width=531, highlightbackground='#AAAAAA', highlightthickness=3, bg="#1A1A1B")
        history_label = Label(top_history, text="Bot Order History:", font=("System", 40, "bold"),
                             fg="#02FF80", bg="#1A1A1B")
        history_label.place(relx=.19, rely=.07)
        top_history.place(relx=.5845, rely=.14)
        tree_frame = Frame(root, highlightbackground='#AAAAAA', highlightthickness=3)
        tree_frame.place(relx=.585, rely=.231)
        #treeview scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        #treeview table
        history_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.configure(command=history_tree.yview)
        history_tree.pack(expand=True, fill='y')
        #columns
        history_tree['columns'] = ("Order Type", "Ticker Symbol", "Shares", "Timestamp")
        history_tree.column("#0", width=0, stretch=NO)
        history_tree.column("Order Type", anchor=CENTER, width=100)
        history_tree.column("Ticker Symbol", anchor=CENTER, width=140)
        history_tree.column("Shares", anchor=CENTER, width=100)
        history_tree.column("Timestamp", anchor=CENTER, width=170)
        #headings
        history_tree.heading("#0", text="", anchor=W)
        history_tree.heading("Order Type", text="Order Type", anchor=CENTER)
        history_tree.heading("Ticker Symbol", text="Ticker Symbol", anchor=CENTER)
        history_tree.heading("Shares", text="Shares", anchor=CENTER)
        history_tree.heading("Timestamp", text="Timestamp", anchor=CENTER)
        # connect order history database
        hconn = sqlite3.connect('order_history.db')
        h = hconn.cursor()
        #def clear tree function
        def clear_all():
            for item in history_tree.get_children():
                history_tree.delete(item)
        #update history constantly
        def update_history():
            clear_all()
            order_data = h.execute("SELECT * FROM history")
            for dt in order_data:
                history_tree.insert("", 'end', values=(dt[0], dt[1], dt[2], dt[3]))
            tree_frame.after(1000, update_history)
        update_history()
        def update_positions():
            position_list = api.list_positions()
            if len(position_list) != 0:
                positions = api.get_position("BTCUSD")
                # if positions is not None:
                symbol = positions.__getattr__('symbol')
                quantity = positions.__getattr__('qty')
                profit = positions.__getattr__('unrealized_pl')
                profit_percent = positions.__getattr__('unrealized_plpc')
                positions_label.config(text=f"Position: {symbol} {quantity} {profit} {profit_percent}")
                positions_identifier.config(text=(" " * 55) + "Symbol:" + (" " * 11) + "Quantity:" + (" " * 9)
                                                 + "Unrealized PL:" + (" " * 50) + "Unrealized PL%: ",
                                            font=("System", 15,),
                                 fg="#02FF80", bg="#1A1A1B")
                root.after(1000, update_positions)
            elif len(position_list) == 0:
                positions_label.config(text=f"Position: None", bg="#1A1A1B")
                positions_identifier.config(text=" ")
                root.after(1000, update_positions)
        positions_label = Label(root, text="", font=("System", 40, "bold"),
                                 fg="#02FF80", bg="#1A1A1B", highlightbackground='#AAAAAA', highlightthickness=3)
        positions_label.place(relx=.1, rely=.85)
        positions_identifier = Label(root, bg="#1A1A1B")
        positions_identifier.place(relx=.1, rely=.816)
        update_positions()
        #################### TRADING BOT #####################

        #bot brain
        bot_frame = Frame(root, height=225, width=531, highlightbackground='#AAAAAA', highlightthickness=3, bg="#1A1A1B")
        symbol_entry = Entry(bot_frame, width=20, borderwidth=1, highlightbackground='#AAAAAA', highlightthickness=1)
        symbol_entry.place(relx=.5, rely=.3, anchor=CENTER)
        symbol_label1 = Label(bot_frame, text="Ticker Symbol: ", font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
        symbol_label1.place(relx=.1, rely=.24)
        top_bot = Label(bot_frame, text="TradeBot Output", font=("System", 20, "bold"),
        fg = "#02FF80", bg = "#1A1A1B", highlightbackground='#AAAAAA', highlightthickness=1)
        top_bot.place(relx=.5, rely=.1, anchor=CENTER)
        Think_Label = Label(bot_frame)
        Possition_Label = Label(bot_frame)
        Sleep_Label = Label(bot_frame)
        def trading_bot():
            BASE_URL = "https://paper-api.alpaca.markets"
            KEY_ID = 'PK5OR2ARKBHAG674ZIHQ'
            SECRET_KEY = '7vbYqdbw1NYrxjYuHuDDkVg0hHtct834sMKRZxKe'
            api = REST(key_id=KEY_ID, secret_key=SECRET_KEY, base_url=BASE_URL)

            SYMBOL = symbol_entry.get()
            SMA_FAST = 12
            SMA_SLOW = 24
            QTY_PER_TRADE = 1

            # create order history database
            conn = sqlite3.connect('order_history.db')
            c = conn.cursor()

            # c.execute("""CREATE TABLE history (Type TEXT, Symbol TEXT, Shares FLOAT, Time TEXT)""")

            def get_pause():
                now = datetime.datetime.now()
                next_min = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
                pause = math.ceil((next_min - now).seconds)
                Sleep_Label.config(text=f"Sleeping for {pause} seconds...", font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
                Sleep_Label.place(relx=.5, rely=.7, anchor= CENTER)
                return pause

            def get_position(symbol):
                positions = api.list_positions()
                for p in positions:
                    if p.symbol == symbol:
                        return float(p.qty)
                return 0

            def get_sma(series, periods):
                return series.rolling(periods).mean()

            # checks whether it should buy (fast ma > slow ma)
            def get_signal(fast, slow):
                return fast[-1] > slow[-1]

            # 1 minute data from alpaca
            def get_bars(symbol):
                bars = api.get_crypto_bars(symbol, TimeFrame.Minute).df
                bars = bars[bars.exchange == 'CBSE']
                bars[f'sma_fast'] = get_sma(bars.close, SMA_FAST)
                bars[f'sma_slow'] = get_sma(bars.close, SMA_SLOW)
                return bars

            while True:
                import datetime
                # get data
                bars = get_bars(symbol=SYMBOL)
                # check positions
                position = get_position(symbol=SYMBOL)
                should_buy = get_signal(bars.sma_fast, bars.sma_slow)
                Think_Label.config(text=f"Position: {position} / Should Buy: {should_buy}", font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
                Think_Label.place(relx=.5, rely=.3, anchor=CENTER)
                if position == 0 and should_buy == True:
                    # buy if buy signal triggered
                    current_order = api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='buy')
                    order_type = current_order.__getattr__('side')
                    symbol1 = current_order.__getattr__('symbol')
                    shares = current_order.__getattr__('qty')
                    timestamp = str(datetime.datetime.now().time())
                    c.execute("INSERT INTO history VALUES "
                              "(:Type, :Symbol, :Shares, :Time)",
                              {'Type': order_type, 'Symbol': symbol1, 'Shares': shares, 'Time': timestamp})
                    conn.commit()
                    Possition_Label.config(text=f'Symbol: {SYMBOL} / Order Type: BUY / Quantity: {QTY_PER_TRADE}', font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
                    Possition_Label.place(relx=.5, rely=.5, anchor=CENTER)
                elif position > 0 and should_buy == False:
                    # sell if sell signal triggered
                    current_order = api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='sell')
                    order_type = current_order.__getattr__('side')
                    symbol1 = current_order.__getattr__('symbol')
                    shares = current_order.__getattr__('qty')
                    timestamp = str(datetime.datetime.now().time())
                    c.execute("INSERT INTO history VALUES "
                              "(:Type, :Symbol, :Shares, :Time)",
                              {'Type': order_type, 'Symbol': symbol1, 'Shares': shares, 'Time': timestamp})
                    conn.commit()
                    Possition_Label.config(text=f'Symbol: {SYMBOL} / Order Type: SELL / Quantity: {QTY_PER_TRADE}', font=("System", 15,), fg="#AAAAAA", bg="#1A1A1B")
                    Possition_Label.place(relx=.5, rely=.5, anchor=CENTER)
                time.sleep(get_pause())
        #run trading bot in background
        def bg_trading():
            if symbol_entry.get() == "BTCUSD":
                threading.Thread(target=trading_bot).start()
                symbol_problem.place_forget()
                symbol_label1.place_forget()
                symbol_entry.place_forget()
                start_button.place_forget()
            else:
                symbol_problem.place(relx=.3, rely=.41)
        symbol_problem = Label(bot_frame, text="Symbol not available. Please try again.", font=("System", 12),
                            fg="red", bg="#1A1A1B")
        #start bot button
        start_button = Button(bot_frame, text="Start Bot", font=("System", 15, "bold"), fg="black",
                          highlightbackground='#02FF80', height=1, width=4, command=bg_trading)
        start_button.place(relx=.5, rely=.65, anchor=CENTER)
        bot_frame.place(relx=.585, rely=.52)
        def graph_data():
            import datetime
            conn = sqlite3.connect('portfolio_equity.db', check_same_thread=False)
            c = conn.cursor()
            # state row #
            row = 0
            # execute once and then comment out
            # c.execute("""CREATE TABLE equity_value (Equity REAL,
            #            Time TEXT, Row INT)""")

            c.execute("DELETE FROM equity_value;")

            def market_hours(start, end, current_time):
                return start <= current_time <= end

            start = datetime.time(0, 0, 0)
            end = datetime.time(23, 59, 59)
            current_time = datetime.datetime.now().time()
            database_time = datetime.datetime.now().time()

            def equity_time():
                account = api.get_account()
                api_equity = account.__getattr__('equity')
                c.execute("INSERT INTO equity_value VALUES (:Equity, :CurrentTime, :Row_Number)", {'Equity': api_equity,
                                                                                                   'CurrentTime': database_time,
                                                                                                   'Row_Number': row})

            while market_hours(start, end, current_time) == True:
                database_time = time.strftime('%H:%M:%S')
                equity_time()
                row += 1
                conn.commit()
                time.sleep(.5)
        def bg_graphing():
            threading.Thread(target=graph_data).start()
        bg_graphing()


#portfolio graph
def portfolio_graph():
    # graph
    matplotlib.use("TkAgg")
    plt.style.use('fivethirtyeight')
    fig = Figure(facecolor="#1A1A1B")
    subplot = fig.add_subplot(111)
    fig.subplots_adjust(left=.11)
    # animation

    def animate(i):
        data = pd.read_sql_table('equity_value', 'sqlite:///portfolio_equity.db')
        x = data['Time']
        y = data['Equity']
        subplot.cla()
        subplot.plot(x, y, color="#02FF80")
        subplot.tick_params(axis='x', colors="#AAAAAA")
        subplot.tick_params(axis='y', colors="#AAAAAA")
        subplot.spines['top'].set_color('#AAAAAA')
        subplot.spines['left'].set_color('#AAAAAA')
        subplot.spines['right'].set_color('#AAAAAA')
        subplot.spines['bottom'].set_color('#AAAAAA')
        subplot.yaxis.set_major_formatter('${x:,.0f}')
        subplot.set_facecolor("#1A1A1B")
        subplot.axes.xaxis.set_visible(False)
        return ani

    # drawing to canvas

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea

    #mouse click
    click_label = Label(root)
    def mouse_event(event):
        mouse_x = int(event.xdata)
        c.execute("SELECT * FROM equity_value WHERE Row=(:Mouse_x)", {'Mouse_x': mouse_x})
        fetch = str(c.fetchall())
        fetch2 = fetch.replace('[', '')
        fetch3 = fetch2.replace(']', '')
        fetch4 = fetch3.replace('(', '$')
        fetch5 = fetch4.replace(')', '')
        fetch6 = fetch5.replace("'", '')
        fetch7 = fetch6.replace("'", '')
        click_label.config(text= fetch7, font=("System", 15,), fg = "#AAAAAA", bg = "#1A1A1B")
        click_label.place(relx=.247, rely=.75)
    fig.canvas.mpl_connect('button_press_event', mouse_event)

    #draw on canvas
    canvas.get_tk_widget().place(x=25, y=120, width=800, height=500)
    canvas.draw()
    ani = FuncAnimation(fig, animate, interval=100)
if __name__ == '__main__':
    login_page()
    root.mainloop()