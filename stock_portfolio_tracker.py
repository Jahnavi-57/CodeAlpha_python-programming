import tkinter as tk
from tkinter import scrolledtext
import requests

API_KEY = '1K90P0CBXFO50FRI'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_data(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        return None

def add_stock():
    global portfolio
    symbol = symbol_entry.get().upper()
    shares = int(shares_entry.get())
    stock_data = get_stock_data(symbol)
    if stock_data:
        price = float(stock_data['05. price'])
        portfolio[symbol] = {'shares': shares, 'price': price}
        output_text.insert(tk.END, f"Added {shares} shares of {symbol} at ${price} each.\n")
    else:
        output_text.insert(tk.END, f"Failed to add {symbol} to portfolio.\n")

def remove_stock():
    global portfolio
    symbol = symbol_entry.get().upper()
    if symbol in portfolio:
        del portfolio[symbol]
        output_text.insert(tk.END, f"Removed {symbol} from portfolio.\n")
    else:
        output_text.insert(tk.END, f"{symbol} not found in portfolio.\n")

def display_portfolio():
    global portfolio
    total_value = 0
    output_text.insert(tk.END, "Portfolio:\n")
    for symbol, data in portfolio.items():
        shares = data['shares']
        price = data['price']
        value = shares * price
        total_value += value
        output_text.insert(tk.END, f"{symbol}: {shares} shares - ${value:.2f}\n")
    output_text.insert(tk.END, f"Total Portfolio Value: ${total_value:.2f}\n")

def clear_output():
    output_text.delete('1.0', tk.END)

def main():
    global symbol_entry, shares_entry, output_text, portfolio
    portfolio = {}

    root = tk.Tk()
    root.title("Stock Portfolio Tracker")
    root.geometry("800x700")
    root.configure(bg="indigo")

    # Symbol Entry
    symbol_label = tk.Label(root, text="Stock Symbol:")
    symbol_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
    symbol_entry = tk.Entry(root)
    symbol_entry.grid(row=0, column=1, padx=10, pady=10)

    # Shares Entry
    shares_label = tk.Label(root, text="Number of Shares:")
    shares_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
    shares_entry = tk.Entry(root)
    shares_entry.grid(row=1, column=1, padx=10, pady=10)

    # Buttons
    add_button = tk.Button(root, text="Add Stock", command=add_stock)
    add_button.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    remove_button = tk.Button(root, text="Remove Stock", command=remove_stock)
    remove_button.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
    display_button = tk.Button(root, text="Display Portfolio", command=display_portfolio)
    display_button.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
    clear_button = tk.Button(root, text="Clear Output", command=clear_output)
    clear_button.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    # Output Text
    output_text = scrolledtext.ScrolledText(root, width=50, height=10)
    output_text.configure(bg="teal")
    output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    # Configure row and column weights
    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()

'''
Apple Inc.: AAPL
Microsoft Corporation: MSFT
Amazon.com Inc.: AMZN
Alphabet Inc. (Google): GOOGL
Tesla, Inc.: TSLA
Netflix, Inc.: NFLX
The Coca-Cola Company: KO
Johnson & Johnson: JNJ
Procter & Gamble Co.: PG
'''
