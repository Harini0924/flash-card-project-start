from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_num=None
random_key = None
data = pandas.read_csv("data/french_words.csv")
data_dict= data.to_dict(orient= "records")
words_dict={}
random_card={}

with open("data/words_to_learn.csv", "r") as file:
    file= pandas.read_csv("data/words_to_learn.csv")
    if(file.empty==True):
        data = pandas.read_csv("data/french_words.csv")
        words_to_learn_csv = data.to_csv("data/words_to_learn.csv")
        words = pandas.read_csv("data/words_to_learn.csv")
        words_dict = words.to_dict(orient="records")
    else:
        words = pandas.read_csv("data/words_to_learn.csv")
        words_dict=words.to_dict(orient="records")


#Will display the next french card
def next_card():
   global random_card
   random_card =random.choice(words_dict)
   random_key=random_card["French"]
   canvas.delete("french_word")
   canvas_image = canvas.create_image(400, 263, image=card_back_img)
   canvas.itemconfig(canvas_image, image=card_front_img)
   canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
   canvas.create_text(400, 263, text=f"{random_key}", font=("Ariel", 60, "bold"),tag="french_word")
   window.after(3000, show_word)

#Will display French cards english translation
def show_word():
    global random_card
    canvas.delete("all")
    canvas_image = canvas.create_image(400, 263, image=card_front_img)
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.create_text(400,150, text="English", font=("Ariel", 40, "italic"), fill="white")
    english_translation = random_card["English"]
    canvas.create_text(400, 263, text=f"{english_translation}", font=("Ariel", 60, "bold"), tag="french_word", fill="white")

def new_card():
    global random_num, random_key
    words_dict.remove(random_card)
    data= pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#UI STUFF
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background= canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word= canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"), tag="french_word")
canvas.grid(column=0,row=0, columnspan=2)

wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0,row=1)
correct_img=PhotoImage(file="images/right.png")
correct_button=Button(image=correct_img, highlightthickness=0, command=new_card)
correct_button.grid(column=1,row=1)

next_card()
window.after(3000,show_word)
window.mainloop()
