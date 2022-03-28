from tkinter import *
import pandas as pd
import random
import time

#UI
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}


def flip_card():
    canvas.itemconfig(language_label, text='English', fill='white')
    canvas.itemconfig(word_label, text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_image, image=back_image)






#logic
def generate_word_mine():

    word = random.choice(list(word_dict.items()))
    print(word['French'])
    canvas.itemconfig(word_label, text=word[0])


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(word_dict)
    canvas.itemconfig(language_label, text='French', fill='black')
    canvas.itemconfig(word_label, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=card_image)
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    global current_card
    global word_dict
    word_dict.remove(current_card)
    df = pd.DataFrame(word_dict)
    df.to_csv('data/words_to_learn.csv', index=False)
    print(len(word_dict))
    generate_word()


window = Tk()
window.title(string="Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

right_image =PhotoImage(file="images/right.png")
wrong_image =PhotoImage(file="images/wrong.png")

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
finally:
    word_dict = data.to_dict(orient="records")



#Buttons
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_button= Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

#Canvas

canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_image)
language_label = canvas.create_text(400, 150, text="French", fill="black", font=LANGUAGE_FONT)
word_label = canvas.create_text(400, 263, text="fityfirity", fill="black", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(padx=50, pady=50, row=0, column=0, columnspan=2)

generate_word()




window.mainloop()



