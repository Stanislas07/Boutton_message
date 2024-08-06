import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__(self, master=None, text="Entrer un nom", command=None, text_color="white", fg_color="8080FF", width=180, height=40, corner_radius=10):
        super().__init__(master, text=text, command=command, text_color=text_color, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius)