# FIRST STOCK PROTOTYPE


import tkinter as tk
from yahoo_fin.stock_info import *

window = tk.Tk()

window.title('Prototype 1 ')
window.geometry('400x200')


# --- FUNCTIONS---

def get_price():
    try:
        price = get_live_price(str(entry1.get()))

    except:
        return "0.00\nINVALID SYMBOL"

    fprice = round(price, 2)

    return fprice


def display_price():
    price = '$' + str(get_price())
    # --- TEXT ---
    display = tk.Text(master=window, height=2, width=15)
    display.grid(column=1, row=2)
    display.insert(tk.END, price)


# --- LABEL ---

label1 = tk.Label(text='ENTER A STOCK SYMBOL : ')
label1.grid(column=0, row=0)

#  --- ENTRY ---

entry1 = tk.Entry()
entry1.grid(column=1, row=0)

# ---- BUTTON ---
button1 = tk.Button(text='Submit', command=display_price)
button1.grid(column=1, row=1)

window.mainloop()
