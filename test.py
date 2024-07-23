from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

def on_button_click():
    messagebox.showinfo(title="message",message="Vous avez réussi !")
    


ttk.Button(root, text="Click me", command = on_button_click).grid(column=1, row=0)

root.mainloop()