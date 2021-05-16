from tkinter import *

root = Tk()


def submit():
    pass


def clear():
    pass


l1 = Label(root, text="Name: ").grid(row=0, column=0)
i1 = Entry(root, width=30).grid(row=0, column=2)

l2 = Label(root, text="Age: ").grid(row=1, column=0)
i2 = Entry(root, width=30).grid(row=1, column=2)

l3 = Label(root, text="Gender: ").grid(row=3, column=0)
i3 = Entry(root, width=30).grid(row=3, column=2)

l4 = Label(root, text="Date of Birth: ").grid(row=4, column=0)
i4 = Entry(root, width=30).grid(row=4, column=2)

btn = Button(root, text="Submit", command=submit).grid(
    row=5, column=0, pady=20, padx=20)

btn2 = Button(root, text="Clear", command=clear).grid(
    row=5, column=1, pady=20, padx=20)

root.mainloop()