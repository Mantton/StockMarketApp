import tkinter as tk
import random

window = tk.Tk()


window.geometry('400x500')
window.title('Bonjour')

#  --- Functions----------
def phrase_gen() :
    phrases = [ 'Hello ', 'Bonjour ', ' Sup ', "What's good "]
    name = str(entry1.get())

    return phrases[random.randint(0, 4)] + name
def phrase_display():
    greeting = phrase_gen()
    #---text field ------
    text1 = tk.Text(master = window, height = 10, width = 30 )
    text1.grid(column= 0, row = 3)
    text1.insert(tk.END, greeting)

# Label

label1 = tk.Label(text = "Test Env")
label1.grid(column = 0, row = 0)


label2 = tk.Label(text = "What is your name? ")
label2.grid(column = 0, row = 1)


# ----- ENTRIES ------------

entry1 = tk.Entry()
entry1.grid(column=1, row=1 )


# ------- BUTTON-------

button1 = tk.Button(text='Submit', command=phrase_display())
button1.grid(column=0, row=2)

# --------------Text field----------





window.mainloop()
