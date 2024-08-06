import customtkinter as ctk

class CustomInput(ctk.CTkEntry):
    def __init__(self, master=None, placeholder_text=None, placeholder_text_color="gray", text_color="black", fg_color="white", width=300, height=30, corner_radius=6):
        super().__init__(master=master, placeholder_text=placeholder_text, placeholder_text_color=placeholder_text_color, text_color=text_color, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius)
