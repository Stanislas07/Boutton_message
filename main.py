import customtkinter as ctk
import tkinter as tk
from widgets.CustomLabel import CustomLabel
from widgets.CustomButton import CustomButton
from widgets.CustomInput import CustomInput
from modules.extraction_tools import process_extract_and_save
from modules.somme import SommeData
from pathlib import Path
from PIL import Image

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Assistance VP28")
        ctk.set_appearance_mode("dark")
        
        # Crée une instance de SommeData
        self.somme_data = SommeData()
        
        # Configure la grille
        self.root.grid_columnconfigure((0, 1), weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        
        #Variable qui va vérifier si les boutons sont sélectionné
        self.plus_clicked = False
        self.moins_clicked = False
        
        #Vérifie que le chemin de l'image existe
        logo_path = Path(__file__).parent / "assets" / "axa-logo.png"
        if logo_path.exists():
            my_image = ctk.CTkImage(Image.open(logo_path), size=(200, 200))
            image_label = ctk.CTkLabel(self.root, image=my_image, text="")
            image_label.grid(row=0, column=0, padx=0, pady=0, sticky="ew", columnspan=2)
        else:
            print(f"Image not found: {logo_path}")

        # Partie gauche(column = 0) PLUS
        self.label_plus = CustomLabel(self.root, text="Emissions de la période", fg_color="#4CAF50")
        self.label_plus.grid(row=1, column=0, padx=20, pady=10, sticky='ew')

        self.ent_plus = CustomInput(self.root, placeholder_text="Entrez un nom de fichier ici", fg_color="#e8f5e9")
        self.ent_plus.grid(row=2, column=0, padx=20, pady=10)

        self.button_plus = CustomButton(self.root, "Fichier Plus", command=self.on_click_file_plus, fg_color="#4CAF50")
        self.button_plus.grid(row=3, column=0, padx=20, pady=10)

        # Partie droite(column = 1) MOINS
        self.label_moins = CustomLabel(self.root, text="Annulations de la période", fg_color="#FF5722")
        self.label_moins.grid(row=1, column=1, padx=20, pady=10, sticky='ew')

        self.ent_moins = CustomInput(self.root, placeholder_text="Entrez un nom de fichier ici", fg_color="#ffebee")
        self.ent_moins.grid(row=2, column=1, padx=20, pady=10)


        self.button_moins = CustomButton(self.root, "Fichier Moins", command=self.on_click_file_moins, fg_color="#FF5722")
        self.button_moins.grid(row=3, column=1, padx=20, pady=10)

        self.result_label = CustomLabel(self.root, text="", text_color="white", fg_color="#1F1F1F",width=180, height=50, corner_radius=8)
        self.result_label.grid(row=4, column=0, padx=20, pady=10, columnspan=2)

        
        
    def on_click_file_plus(self):
        input_value_plus = self.ent_plus.get()
        sum_EMI = process_extract_and_save(input_value_plus, negate=False)
        self.somme_data.set_sum_EMI(sum_EMI)
        self.plus_clicked = True
        self.check_and_calcul()

    def on_click_file_moins(self):
        input_value_less = self.ent_moins.get()
        sum_EMI_ANNUL = process_extract_and_save(input_value_less, negate=True)
        self.somme_data.set_sum_EMI_ANNUL(sum_EMI_ANNUL)
        self.moins_clicked = True
        self.check_and_calcul()

    def check_and_calcul(self):
        if self.plus_clicked and self.moins_clicked:
            sum_total = self.somme_data.get_sum_EMI() + self.somme_data.get_sum_EMI_ANNUL()
            self.result_label.configure(text=f"Montant total des émissions: {sum_total}")

    def refresh():
        root.reset()
root = ctk.CTk()
app = App(root)
root.mainloop()
