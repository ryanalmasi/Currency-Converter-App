import tkinter as tk
from tkinter import font
import requests
# https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}
# VI3dJmrPuC15oDjDnZmFGGAhvjqiK6RB

"""
Simple intializations: app window and sizing variables.
"""
app = tk.Tk()
HEIGHT = 700
WIDTH = 800


"""
App Functions: -convert_currency uses the fixer api to convert given currency to whatever is desired
               -format_response then displays retrieved data from created json file to then output
                onto text box in app
"""
def convert_currency(amount, frm, to):
    key = {"apikey" : "VI3dJmrPuC15oDjDnZmFGGAhvjqiK6RB"}
    url = "https://api.apilayer.com/fixer/convert?"
    parameters = {'to': to, 'amount': amount, 'from': frm}
    response = requests.get(url, headers = key, params = parameters)
    currency = response.json()

    label['text'] = format_response(currency)

def format_response(currency):
    try:
        amnt = currency['query']['amount']
        frm = currency['query']['from']
        to = currency['query']['to']
        total = currency['result']
        final = str(amnt) + ' ' + frm + ' to ' + to + ': ' + '$' + str("%.2f" % total)
    except:
        final = 'We ran into a problem retrieving that information, please try again!'
    
    return final


"""
Tkinter styling positional arguments. Here the widgets, buttons, input, and output text boxes are 
created and placed.
"""
canvas = tk.Canvas(app, height = HEIGHT, width = WIDTH, bg="#1f1f1f")
canvas.pack()

upper_frame = tk.Frame(app, bg='#1f1f1f')
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor="n")

frame = tk.Frame(app, bg="#1f1f1f")
frame.place(relx= 0.5, rely= 0.2, relwidth=0.75, relheight=0.05, anchor="n")

lower_frame = tk.Frame(app, bg="#1f1f1f")
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor="n")

entry_amount = tk.Entry(frame, bg="white", fg="black", font=('Courier', 15))
entry_amount.place(relwidth=0.2, relheight=1,)
entry_amount.insert(index=0, string="*AMOUNT*")

entry_base = tk.Entry(frame, bg="white", fg="black", font=('Courier', 15))
entry_base.place(relx=0.22, relwidth=0.26, relheight=1)
entry_base.insert(index=0, string="*BASE*")

entry_currency = tk.Entry(frame, bg="white", fg="black", font=('Courier', 15))
entry_currency.place(relx=0.5, relwidth=0.25, relheight=1)
entry_currency.insert(index=0, string="*TO CONVERT*")

button = tk.Button(frame, text="CONVERT", bg="grey", fg="white", font=('Courier', 15), 
    command=lambda: convert_currency(entry_amount.get(),entry_base.get() ,entry_currency.get()))
button.place(relx=0.77, relheight=1, relwidth=0.25)

label = tk.Label(lower_frame, bg="white", font=('Courier', 10))
label.place(relheight=1, relwidth=1)

title = tk.Label(upper_frame, bg='#1f1f1f', fg='white', font=('Courer', 25), text='$ CURRENCY CONVERTER $')
title.place(relheight=1, relwidth=1)


app.mainloop() # Calls and launches app.
