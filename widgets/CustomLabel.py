import customtkinter as ctk

class CustomLabel(ctk.CTkLabel):
    def __init__(self, master=None, text="Entrer un nom", text_color="white", fg_color="white", width=200, height=30, corner_radius=6):
        super().__init__(master=master, text=text, text_color=text_color, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius)
