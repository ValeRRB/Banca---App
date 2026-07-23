import customtkinter
from PIL import Image
from utils import resource_path

class Frame_Cronologia(customtkinter.CTkFrame):
     def __init__(self, master, database):
          super().__init__(master)
          self.database = database

class Frame_Avvisi(customtkinter.CTkFrame):
    def __init__(self, master, database):
            super().__init__(master)
            self.database = database

class Frame_Ultima_Attività(customtkinter.CTkFrame):
    def __init__(self, master, database):
            super().__init__(master)
            self.database = database

class Frame_PieChart(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

class Finestra_CreaConto(customtkinter.CTkToplevel):
    def __init__(self, master, database, codicefiscale, caricamento_conto):
        super().__init__(master)
        self.database = database
        self.codicefiscale = codicefiscale
        self.caricamento_conto = caricamento_conto

        self.title("Crea Nuovo Conto")
        self.geometry("380x320")
        self.resizable(False, False)

        self.transient(master)
        self.grab_set()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.label_titolo = customtkinter.CTkLabel(self, 
                                                     text="Nuovo Conto Bancario",
                                                     font=("Arial", 18, "bold"))
        self.label_titolo.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.input_combo_tipo = customtkinter.CTkOptionMenu(self,
                                                              values=["Standard", "Risparmi", "Business"],
                                                              width=280)
        self.input_combo_tipo.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.pulsante_crea = customtkinter.CTkButton(self,
                                                       text="Crea Conto",
                                                       font=("Arial", 18),
                                                       command=self.salva_conto)
        self.pulsante_crea.grid(row=2, column=0, padx=20, pady=20)

    def salva_conto(self):
        self.tipologia_conto = self.input_combo_tipo.get()

        self.database.creaConto(self.codicefiscale, tipoconto=self.tipologia_conto)

        if self.caricamento_conto:
            self.caricamento_conto()

        self.destroy()


class Frame_Conto(customtkinter.CTkFrame):
    def __init__(self, master, database, codicefiscale, account_informazioni, caricamento_slot):
        super().__init__(master)
        self.database = database
        self.codicefiscale = codicefiscale
        self.account_informazioni = account_informazioni
        self.caricamento_slot = caricamento_slot

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.carica_dati()

    def carica_dati(self):
        for elemento in self.winfo_children():
            elemento.destroy()

        if self.account_informazioni:
            self.iban, self.saldo, self.tipo_conto, self.stato = self.account_informazioni

            self.iban_visualizzato = f"...{self.iban[-4:]}"
            self.numero_carte = 0

            self.label_titolo_conto = customtkinter.CTkLabel(self,
                                                             text=f"Conto {self.tipo_conto.upper()}",
                                                             font=("Arial", 11, "bold"))
            self.label_titolo_conto.grid(row=0, column=0, padx=10, pady=10)

            self.label_saldo_conto = customtkinter.CTkLabel(self,
                                                            text=f"€ {self.saldo:,.2f}",
                                                            font=("Arial", 22, "bold"))
            self.label_saldo_conto.grid(row=1, column=0, padx=10, pady=(0, 10))

            self.label_iban_conto = customtkinter.CTkLabel(self,
                                                           text=f"IBAN: {self.iban_visualizzato}",
                                                           font=("Arial", 10)) 
            self.label_iban_conto.grid(row=2, column=0, padx=10, pady=(0, 10))

            self.label_numeroCarte_conto = customtkinter.CTkLabel(self,
                                                                  text=f"Carte attive: {self.numero_carte} 💳",
                                                                  font=("Arial", 11)) 
            self.label_numeroCarte_conto.grid(row=3, column=0, padx=10, pady=(0, 10))

        else:
            self.label_contenuto_vuoto = customtkinter.CTkLabel(self,
                                                                text="Slot disponibile",
                                                                font=("Arial", 12))
            self.label_contenuto_vuoto.grid(row=0, column=0, padx=20, pady=10)

            self.pulsante_crea_conto = customtkinter.CTkButton(self,
                                                               text="+ Crea Conto",
                                                               font=("Arial", 18),
                                                               height=50,
                                                               command=self.apri_finestra_creazione_conto)
            self.pulsante_crea_conto.grid(row=3, column=0, padx=20, pady=10)

    def apri_finestra_creazione_conto(self):
        self.finestra_creaconto = Finestra_CreaConto(self, self.database, self.codicefiscale, self.caricamento_slot)
        
         


class Frame_Dashboard_Content(customtkinter.CTkScrollableFrame):
    def __init__(self, master, database, codicefiscale):
        super().__init__(master)
        self.database = database
        self.codicefiscale = codicefiscale

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=0, minsize=50)
        self.rowconfigure(1, weight=0, minsize=150)
        self.rowconfigure(2, weight=0, minsize=50)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=0, minsize=50)
        self.rowconfigure(6, weight=1)

        self.label_titolo_conti = customtkinter.CTkLabel(self,
                                                         text="Conti",
                                                         font=("Arial", 30, "bold"))
        self.label_titolo_conti.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsw")

        self.carica_slot_conti()

        self.label_titolo_dati = customtkinter.CTkLabel(self,
                                                        text="Panoramica",
                                                        font=("Arial", 30, "bold"))
        self.label_titolo_dati.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="nsw")

        self.frame_piechart = Frame_PieChart(self, self.database)
        self.frame_piechart.grid(row=3, column=0, rowspan=2, columnspan=2, padx=(20, 10), pady=10, sticky="nsew")

        self.frame_ultima_attività = Frame_Ultima_Attività(self, self.database)
        self.frame_ultima_attività.grid(row=3, column=2, padx=(10, 20), pady=10, sticky="nsew")

        self.frame_avvisi = Frame_Avvisi(self, self.database)
        self.frame_avvisi.grid(row=4, column=2, padx=(10, 20), pady=10, sticky="nsew")

        self.label_titolo_cronologia = customtkinter.CTkLabel(self,
                                                              text="Cronologia",
                                                              font=("Arial", 30, "bold"))
        self.label_titolo_cronologia.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="nsw")

        self.frame_cronologia = Frame_Cronologia(self, self.database)
        self.frame_cronologia.grid(row=6, column=0, columnspan=3, padx=20, pady=(10, 20), sticky="nsew")

    def carica_slot_conti(self):
        self.conti_utente = []
        if hasattr(self.database, "getContiUtente"):
            self.conti_utente = self.database.getContiUtente(self.codicefiscale)

        for slot in range(3):
            self.account_informazioni = self.conti_utente[slot] if slot < len(self.conti_utente) else None

            self.padx = (20, 10) if slot == 0 else ((10, 20) if slot == 2 else (10, 10))

            self.frame_conto = Frame_Conto(self, self.database, self.codicefiscale, self.account_informazioni, self.carica_slot_conti)
            self.frame_conto.grid(row=1, column=slot, padx=self.padx, pady=10, sticky="nsew")


        

class Dashboard(customtkinter.CTkFrame):
    def __init__(self, master, database, sessione_utente):
        super().__init__(master, corner_radius=0)
        self.database = database
        self.sessione_utente = sessione_utente

        self.email = self.sessione_utente[0]
        self.codicefiscale = self.database.getCodiceFiscaleByEmail(self.email)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0, minsize=50)
        self.rowconfigure(1, weight=1)

        self.label_titolo = customtkinter.CTkLabel(self,
                                                   text="Dashboard",
                                                   font=("Arial", 30, "bold"),
                                                   compound="left")
        self.label_titolo.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="nsw")

        self.frame_dashboard_content = Frame_Dashboard_Content(self, self.database, self.codicefiscale)
        self.frame_dashboard_content.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="nsew")
