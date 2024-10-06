import tkinter as tk
import customtkinter as ctk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import mysql.connector as m

# Connect to the MySQL database
try:
    cob = m.connect(host='localhost', user='root', password='Aadivnt24#', database='hackathon')
    cursorob = cob.cursor()
except m.Error as e:
    print(f"Error connecting to MySQL database: {e}")
    exit()

def fetch_stock_data(symbol):
    """Fetch stock data for a given symbol."""
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period='1d', interval='1m')
        if df.empty:
            raise ValueError(f"No data found for symbol: {symbol}")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def plot_stock(symbol):
    """Plot the stock data for a given symbol."""
    df = fetch_stock_data(symbol)
    if df is None:
        return plt.figure()  # Return an empty figure in case of error

    times = df.index.strftime('%H:%M:%S')
    prices = df['Close']

    fig, ax = plt.subplots()
    ax.plot(times, prices, label=f"{symbol} Price")
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.set_title(f"{symbol} Stock Price on {datetime.now().strftime('%Y-%m-%d')}")
    ax.legend()

    return fig

def update_plot():
    """Update the plot every minute."""
    fig = plot_stock(stock_symbol)
    canvas.figure = fig
    canvas.draw()
    root.after(60000, update_plot)

# Create the Tkinter window
root = ctk.CTk()
root.title("Live Stock Price")
root.geometry("800x600")

# Fetch the stock symbol from the database
cursorob.execute('SELECT * FROM data')
results = cursorob.fetchall()

# Change this to the desired company name
company_name = 'Infosys Ltd.'
stock_symbol = None

for record in results:
    if record[1] == company_name:
        stock_symbol = record[2]  # Store the company symbol
        break

if stock_symbol is None:
    print(f"Stock symbol not found for the specified company: {company_name}")
    exit()

# Initial plot
fig = plot_stock(stock_symbol)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the update loop
update_plot()

# Start the Tkinter main loop
root.mainloop()
