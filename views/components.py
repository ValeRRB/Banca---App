import customtkinter
from PIL import Image
from utils import resource_path

class Utente(customtkinter.CTkFrame):
    def __init__(self, master, database, mostra_pagina_callback):
        super().__init__(master)
        self.database = database
        self.mostra_pagina = mostra_pagina_callback

class Frame_Utente(customtkinter.CTkFrame):
    def __init__(self, master, database, mostra_pagina_callback, sessione_utente):
        super().__init__(master, corner_radius=10)
        self.database = database
        self.mostra_pagina = mostra_pagina_callback
        self.sessione_utente = sessione_utente

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)

        self.profilo_utente_icona = customtkinter.CTkImage(Image.open(resource_path(r"assets\user.png")),
                                                           size=(80, 80))
        self.profilo_utente_icona_label = customtkinter.CTkLabel(self,
                                                                 image=self.profilo_utente_icona,
                                                                 text=None)
        self.profilo_utente_icona_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        self.profilo_utente_label_username = customtkinter.CTkLabel(self,
                                                                   text=f"{self.sessione_utente[3]} {self.sessione_utente[4]}",
                                                                   font=("Arial", 18), 
                                                                   fg_color="transparent")
        self.profilo_utente_label_username.grid(row=0, column=1, padx=10, sticky="s")

        self.pulsante_impostazioni = customtkinter.CTkButton(self,
                                                             text="Informazioni Utente",
                                                             font=("Arial", 18),
                                                             corner_radius=10,
                                                             width=200,
                                                             height=40,
                                                             command=self.visualizza_informazioni_utente)
        self.pulsante_impostazioni.grid(row=1, column=1, padx=10, pady=(5, 10))

    def visualizza_informazioni_utente(self):
        self.mostra_pagina("Utente")

class Dashboard(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master, corner_radius=0)
        self.database = database

class Carta(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master, corner_radius=0)
        self.database = database