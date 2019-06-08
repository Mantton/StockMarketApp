# GUI Test environment

import tkinter as tk

window = tk.Tk()


window.title('TEST ENVIRONMENT')  # title
window.geometry('400x400')  # Dimension

#  . label, .button, .entry, .text

# LABEL
title = tk.Label(text='Hello World,\n Testing GUI environment', font = ('Times New Roman', 20))
title.grid(column=0,row=0)

# Button
button1 = tk.Button(text="TEST1", bg = 'red')
button1.grid(column=0, row=1)

# Entry field 1
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

# Text Field
text_field1 = tk.Text(master=window, height = 5, width = 10 )
text_field1.grid(column=0, row=3)






window.mainloop()