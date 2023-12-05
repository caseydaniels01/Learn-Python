
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Example")
my_label.pack()

# my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

#Entry

input = tkinter.Entry(width=10)
input.pack()
print(input.get())







window.mainloop()