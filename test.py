from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def on_button_click():
    frm = ttk.Frame(root, padding=10)
    

ttk.Label(frm, text="Vous avez réussi !").grid(column=0, row=0)
ttk.Button(frm, texte="Click me", commande = on_button_click).grid(column=1, row=0)

root.mainloop()