import customtkinter
from PIL import Image
from utils import resource_path

class App_Finestra_Signin(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master, fg_color="transparent")
        self.database = database

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)
        self.rowconfigure(7, weight=0)
        self.rowconfigure(8, weight=0)
        self.rowconfigure(9, weight=0)
        self.rowconfigure(10, weight=0)
        self.rowconfigure(11, weight=0)

        self.icona_login = customtkinter.CTkImage(Image.open(resource_path(r"assets\icon.ico")),
                                                           size=(80, 80))
        self.label_icona_login = customtkinter.CTkLabel(self,
                                                        image=self.icona_login,
                                                        text=" CoreCapital Bank",
                                                        font=("Arial", 50, "bold"),
                                                        compound="left")
        self.label_icona_login.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30))

        self.label_titolo_login_1 = customtkinter.CTkLabel(self, 
                                                         text="Benvenuto", 
                                                         font=("Arial", 30, "bold"), 
                                                         fg_color="transparent",)
        self.label_titolo_login_1.grid(row=1, column=0, columnspan=2, padx=(45, 20), pady=(20, 0), sticky="w")

        self.label_titolo_login_2 = customtkinter.CTkLabel(self, 
                                                         text="Inserire tutti i dati richiesti per aprire un conto. Successivamente potrai creare una carta:",
                                                         font=("Arial", 18), 
                                                         fg_color="transparent")
        self.label_titolo_login_2.grid(row=2, column=0, columnspan=2, padx=(45, 20), pady=10, sticky="w")

        self.input_codicefiscale = customtkinter.CTkEntry(self,
                                                   placeholder_text="Codice fiscale",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_codicefiscale.grid(row=3, column=0, padx=(20, 10), pady=(20,0))

        self.input_email = customtkinter.CTkEntry(self,
                                                   placeholder_text="Email",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_email.grid(row=4, column=0, padx=(20, 10), pady=(20,0))

        self.input_password = customtkinter.CTkEntry(self,
                                                   placeholder_text="Password",
                                                   show="*",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_password.grid(row=5, column=0, padx=(20, 10), pady=(20,0))

        self.input_cognome = customtkinter.CTkEntry(self,
                                                   placeholder_text="Cognome",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_cognome.grid(row=6, column=0, padx=(20, 10), pady=(20,0))

        self.input_nome = customtkinter.CTkEntry(self,
                                                   placeholder_text="Nome",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_nome.grid(row=7, column=0, padx=(20, 10), pady=(20,0))

        self.input_cittànascita = customtkinter.CTkEntry(self,
                                                   placeholder_text="Città di nascita",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_cittànascita.grid(row=3, column=1, padx=(10, 20), pady=(20,0))

        self.input_datanascita = customtkinter.CTkEntry(self,
                                                   placeholder_text="Data di nascita",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_datanascita.grid(row=4, column=1, padx=(10, 20), pady=(20,0))

        self.input_residenza = customtkinter.CTkEntry(self,
                                                   placeholder_text="Residenza",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_residenza.grid(row=5, column=1, padx=(10, 20), pady=(20,0))

        self.input_cittadinanza = customtkinter.CTkEntry(self,
                                                   placeholder_text="Cittadinanza",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_cittadinanza.grid(row=6, column=1, padx=(10, 20), pady=(20,0))

        self.input_numerocellulare = customtkinter.CTkEntry(self,
                                                   placeholder_text="Numero cellulare",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_numerocellulare.grid(row=7, column=1, padx=(10, 20), pady=(20,0))

        self.label_linea_separazione = customtkinter.CTkLabel(self,
                                                              text="________________________________________________________________________________________________________________________________________________",
                                                              font=("Arial", 10),
                                                              compound="left")
        self.label_linea_separazione.grid(row=8, column=0, columnspan=2, padx=20, pady=20)

        self.pulsante_registrati = customtkinter.CTkButton(self,
                                                         text="Registrati",
                                                         font=("Arial", 20),
                                                         corner_radius=10,
                                                         width=400,
                                                         height=50,
                                                         command=self.signin)
        self.pulsante_registrati.grid(row=9, column=0, columnspan=2, padx=20, pady=(0, 20))


        self.label_domanda_registrazione = customtkinter.CTkLabel(self,
                                                              text="Hai già un account?",
                                                              font=("Arial", 18),
                                                              compound="left")
        self.label_domanda_registrazione.grid(row=10, column=0, columnspan=2, padx=20, pady=10)

        self.pulsante_accesso = customtkinter.CTkButton(self,
                                                         text="Fai l'accesso",
                                                         font=("Arial", 20),
                                                         corner_radius=10,
                                                         width=400,
                                                         height=50,
                                                         command=self.passaggio_login)
        self.pulsante_accesso.grid(row=11, column=0, columnspan=2, padx=20, pady=(10, 20))

    def signin(self):
        codicefiscale = self.input_codicefiscale.get()
        email = self.input_email.get()
        password = self.input_password.get()
        cognome = self.input_cognome.get()
        nome = self.input_nome.get()
        cittànascita = self.input_cittànascita.get()
        datanascita = self.input_datanascita.get()
        residenza = self.input_residenza.get()
        cittadinanza = self.input_cittadinanza.get()
        numerocellulare = self.input_numerocellulare.get()

        self.database.signin(codicefiscale, email, password, cognome, nome, cittànascita, datanascita, residenza, cittadinanza, numerocellulare)

        self.open_main_app(self.database.login(email, password))

    def passaggio_login(self):
        from views.login import Frame_Finestra_Login
        self.destroy()

        self.master.title("CoreCapital - Login")
        self.master.geometry("600x750")
        self.master.resizable(False, False)

        self.finestra_login = Frame_Finestra_Login(self.master, self.database)
        self.finestra_login.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def open_main_app(self, sessione_utente):
        from views.main_app import MainApp
        self.destroy()

        self.master.geometry("1400x900")
        self.master.title("CoreCapital")
        self.master.resizable(True, True)

        self.sessione_utente = sessione_utente

        self.main_app = MainApp(self.master, self.database, self.sessione_utente)
        self.main_app.grid(row=0, column=0, sticky="nsew")