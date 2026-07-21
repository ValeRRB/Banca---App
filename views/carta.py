import customtkinter
from PIL import Image
from utils import resource_path

class Frame_Carta(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

class Frame_Azioni_Carta(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

class Frame_Cronologia_Transazioni(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

class Carta(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master, corner_radius=0)
        self.database = database

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

        self.frame_carta = Frame_Carta(self, self.database)
        self.frame_carta.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        self.frame_azioni_carta = Frame_Azioni_Carta(self, self.database)
        self.frame_azioni_carta.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="nsew")

        self.frame_cronologia_transazioni = Frame_Cronologia_Transazioni(self, self.database)
        self.frame_cronologia_transazioni.grid(row=1, column=1, padx=(10, 20), pady=20, sticky="nsew")

