from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"




#--------- PANDAS ----------#

data = pandas.read_csv(r"C:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\Flashcards\data\french_words.csv")
data_dict = data.to_dict(orient="records")
# rand_choose = random.choice(list(data_dict))
# fr_word = list(rand_choose.values())[:1]
# en_word = list(rand_choose.values())[1:]
# print(fr_word)
# print(en_word)


#--------- BUTTONS ----------#

def red_button_func():
    rand_choose = random.choice(list(data_dict))
    fr_word = list(rand_choose.values())[:1]
    fr_word = [fr_word.replace("{","") for item in fr_word]
    fr_word = [fr_word.replace("}","") for item in fr_word]
    en_word = list(rand_choose.values())[1:]
    en_word = [en_word.replace("{","") for item in en_word]
    en_word = [en_word.replace("{","") for item in en_word]
    word.config(text=en_word)


def green_button_func():
    rand_choose = random.choice(list(data_dict))
    fr_word = list(rand_choose.values())[:1]
    fr_word1 = fr_word.replace("{","")
    fr_word2 = fr_word1.replace("}","")
    en_word = list(rand_choose.values())[1:]
    en_word1 = en_word.replace("{","")
    en_word2 = en_word1.replace("}","")
    word.config(text=en_word2)


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
word = Label(text="", font=("Ariel", 60, "bold"), bg="white")
word.place(x=350,y=263)

red_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\Flashcards\images\wrong.png")
green_img = PhotoImage(file=r"C:\Users\casey\OneDrive\Desktop\Code - VSCode\Learn-Python\Learn-Python\Flashcards\images\right.png")

red_button = Button(image=red_img, highlightthickness=0, command=red_button_func)
red_button.grid(row=1, column=0)
green_button = Button(image=green_img, highlightthickness=0, command=green_button_func)
green_button.grid(row=1, column=1)

window.mainloop()