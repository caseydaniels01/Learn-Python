from tkinter import *


def button_clicked():
    new_text = float(input.get())
    calc = round(new_text * 1.609344,2)
    total.config(text=calc)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=90)
window.config(padx=100)


Miles = Label(text="Miles")
Miles.grid(column=2, row=0)
Miles.config(padx=20)

Km = Label(text="Km")
Km.grid(column=2, row=1)
Km.config(padx=20)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)
is_equal.config(padx=20)

total = Label()
total.grid(column=1, row=1)
total.config(pady=10)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)









window.mainloop()