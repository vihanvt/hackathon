import tkinter as tk
import customtkinter as ctk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import threading
import mysql.connector as m

cob=m.connect(host='localhost',user='root',password='9636103034',database='hackathon')
cursorob=cob.cursor()


# Fetch stock data from yfinance
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period='1d', interval='1m')
    return df

# Plot stock graph using matplotlib
def plot_stock(symbol):
    df = fetch_stock_data(symbol)
    times = df.index.strftime('%H:%M:%S')
    prices = df['Close']

    fig, ax = plt.subplots()
    ax.plot(times, prices, label=f"{symbol} Price")
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.set_title(f"{symbol} Stock Price on {datetime.now().strftime('%Y-%m-%d')}")
    ax.legend()

    return fig

# Function to update the plot periodically
def update_plot():
    fig = plot_stock(stock_symbol)
    
    # Clear old plot and replace with the new one
    canvas.figure = fig
    canvas.draw()
    
    # Call this function every 60 seconds
    root.after(60000, update_plot)

# Create the Tkinter window
root = ctk.CTk()
root.title("Live Stock Price")
root.geometry("800x600")

# Stock symbol

cursorob.execute('select * from data')
r=cursorob.fetchall()
x = '' #Mention the company you want
for i in r:
    if i[1] == x:
        a = i[2] #Storing the company symbol
        
stock_symbol = "{}".format(a)  # You can change this to any stock symbol

# Create and embed the initial plot in the Tkinter window

fig = plot_stock(stock_symbol)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start updating the plot periodically
update_plot()

# Run the mainloop
root.mainloop()
