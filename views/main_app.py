import customtkinter
from PIL import Image
from utils import resource_path
from views.components import Utente, Frame_Utente
from views.dashboard import Dashboard
from views.carta import Carta

class Frame_Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, database, mostra_pagina_callback, sessione_utente):
        super().__init__(master, fg_color="transparent")
        self.database = database
        self.mostra_pagina = mostra_pagina_callback
        self.sessione_utente = sessione_utente

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)

        self.label_logo_image = customtkinter.CTkImage(Image.open(r"assets\icon.ico"),
                                                        size=(35, 35))
        self.label_logo = customtkinter.CTkLabel(self,
                                                 image=self.label_logo_image,
                                                 text="  CoreCapital Bank",
                                                 compound="left",
                                                 font=("Arial", 30, "bold"))
        self.label_logo.grid(row=0, column=0, padx=20, pady=20, sticky="new")

        self.label_titolo = customtkinter.CTkLabel(self, 
                                                   text="Menu principale", 
                                                   font=("Arial", 20), 
                                                   fg_color="transparent")
        self.label_titolo.grid(row=1, column=0, padx=20, pady=(10, 0))

        self.pulsante_dashboard = customtkinter.CTkButton(self,
                                                     text="Dashboard",
                                                     corner_radius=10,
                                                     font=("Arial", 18),
                                                     height=50,
                                                     command=self.pulsante_passaggio_dashboard)
        self.pulsante_dashboard.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="new")

        self.pulsante_carta1 = customtkinter.CTkButton(self,
                                                     text="Carta 1",
                                                     corner_radius=10,
                                                     font=("Arial", 18),
                                                     height=50,
                                                     command=self.pulsante_passaggio_carta1)
        self.pulsante_carta1.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="new")

        self.frame_utente = Frame_Utente(self, self.database, self.mostra_pagina, self.sessione_utente)
        self.frame_utente.grid(row=5, column=0, padx=20, pady=20, sticky="sew")

    def pulsante_passaggio_dashboard(self):
        self.mostra_pagina("Dashboard")

    def pulsante_passaggio_carta1(self):
        self.mostra_pagina("Carta1")

class Frame_Principale(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent", corner_radius=0)

class MainApp(customtkinter.CTkFrame):
    def __init__(self, master, database, sessione_utente):
        super().__init__(master, fg_color="transparent")
        self.database = database
        self.sessione_utente = sessione_utente

        self.columnconfigure(0, weight=0, minsize=300)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.sidebar = Frame_Sidebar(self, self.database, self.mostra_pagina, self.sessione_utente)
        self.sidebar.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_principale = Frame_Principale(self)
        self.frame_principale.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        self.pagine_frame = {
            "Dashboard": Dashboard(self.frame_principale, self.database, self.sessione_utente),
            "Carta1": Carta(self.frame_principale, self.database),
            "Utente": Utente(self.frame_principale, self.database, self.mostra_pagina)
        }

        for pagina in self.pagine_frame.values():
            pagina.place(relwidth=1, relheight=1)

        self.mostra_pagina("Dashboard")

    def mostra_pagina(self, nome):
        frame = self.pagine_frame[nome]
        frame.lift()