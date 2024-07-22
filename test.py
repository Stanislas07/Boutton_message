from tkinter import *
from tkinter import ttk

def on_button_click():
    messagebox.showinfo("Message","Vous avez réussi !")
    
root = Tk()
root.title("First page")

boutton = ttk.Button(root, texte="Click me", commande = on_button_click)
boutton = pack(pady=20)

root.mainloop()