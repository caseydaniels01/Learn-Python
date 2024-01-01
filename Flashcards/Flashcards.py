from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#--------- PANDAS ----------#
try:
    data = pandas.read_csv(r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\data\french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\data\french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


#--------- BUTTONS ----------#

def red_button_func():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def green_button_func():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\data\words_to_learn.csv", index=False)
    green_button_func()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


#--------- UI ----------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=550, width=900)
card_front_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\images\card_front.png")
card_back_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

red_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\images\wrong.png")
green_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code\Learn-Python\Flashcards\images\right.png")

red_button = Button(image=red_img, highlightthickness=0, command=red_button_func)
red_button.grid(row=1, column=0)
green_button = Button(image=green_img, highlightthickness=0, command=green_button_func)
green_button.grid(row=1, column=1)

green_button_func()

window.mainloop()