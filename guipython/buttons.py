from tkinter import *
import random
root = Tk()

def choose():
    words = ["hello", "harry potter", "linkin park", "marvel"]
    my_label = Label(text=random.choice(words))
    my_label.pack()
btn = Button(text="screaming button!!!", command=choose)
btn.pack()

root.mainloop()