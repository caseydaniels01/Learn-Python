from tkinter import *
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"












#--------- UI ----------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

canvas = Canvas(height=550, width=900)
card_front = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\Flashcards\images\card_front.png")
canvas.create_image(460,275, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

lang = Label(text="French", font=("Ariel", 40, "italic"), bg="white")
lang.place(x=350,y=150)
word = Label(text="trouve", font=("Ariel", 60, "bold"), bg="white")
word.place(x=350,y=263)

red_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\Flashcards\images\wrong.png")
green_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\Flashcards\images\right.png")

red_button = Button(image=red_img, highlightthickness=0)
red_button.grid(row=1, column=0)
green_button = Button(image=green_img, highlightthickness=0)
green_button.grid(row=1, column=1)

window.mainloop()