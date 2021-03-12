import pandas as pd
from tkinter import *
import random


#-------------------------------Working Logic--------------------------#
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#fff"
current_card = {}
words_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    words_dict = data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    French_word = current_card["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=French_word,fill="black")
    canvas.itemconfig(card_background,image=front_image)
    flip_timer = window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_image)

def is_known():
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()



#--------------------------------UI Setup------------------------------#


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)




flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400,150,text="",font=("Aerial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Aerial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

#Buttons
check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)


next_card()





















window.mainloop()