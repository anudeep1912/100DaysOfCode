from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
BUTTON_HIGHLIGHT_COLOR = "#FFAFAF"
FONT_NAME = "Ariel"
current_word = {}
learn_list = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn_list = original_data.to_dict(orient="records")
else:
    learn_list = data.to_dict(orient="records")
# ------------------------ Extracting Data --------------------------- #


def next_card():
    """Displays a Random word in french and flips the card after 3 seconds"""
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(learn_list)
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="French", fill="white")
    canvas.itemconfig(card_text, text=current_word["French"], fill="white")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """Displays the word translation in English"""
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_text, text=current_word["English"], fill="black")


def is_known():
    """Removes the word from the list if user answers correctly"""
    learn_list.remove(current_word)
    correct_data = pandas.DataFrame(learn_list)
    correct_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=400, height=263, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(200, 125, image=card_back)
card_title = canvas.create_text(200, 100, text="", fill="white", font=(FONT_NAME, 15, "italic"))
card_text = canvas.create_text(200, 150, text="", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=0, column=1, columnspan=2, padx=50, pady=(20, 0))


yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, command=is_known, width=50, height=50, highlightthickness=0)
yes_button.grid(row=1, column=1, padx=(30, 0), pady=(5, 20))
yes_button.config(bd=0)

no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, command=next_card, width=50, height=50, highlightthickness=0)
no_button.grid(row=1, column=2, padx=(0, 30), pady=(5, 20))
no_button.config(bd=0)

next_card()

window.mainloop()







