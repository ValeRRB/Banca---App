import customtkinter
from PIL import Image
from utils import resource_path

class Frame_Finestra_Login(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master, fg_color="transparent")
        self.database = database
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)
        self.rowconfigure(7, weight=0)
        self.rowconfigure(8, weight=0)

        self.icona_login = customtkinter.CTkImage(Image.open(resource_path(r"assets\icon.ico")),
                                                           size=(80, 80))
        self.label_icona_login = customtkinter.CTkLabel(self,
                                                        image=self.icona_login,
                                                        text=" CoreCapital Bank",
                                                        font=("Arial", 50, "bold"),
                                                        compound="left")
        self.label_icona_login.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.label_titolo_login_1 = customtkinter.CTkLabel(self, 
                                                         text="Bentornato", 
                                                         font=("Arial", 30, "bold"), 
                                                         fg_color="transparent",)
        self.label_titolo_login_1.grid(row=1, column=0, padx=(80, 20), pady=(20, 0), sticky="w")

        self.label_titolo_login_2 = customtkinter.CTkLabel(self, 
                                                         text="Effettuare l'accesso per proseguire:", 
                                                         font=("Arial", 18), 
                                                         fg_color="transparent")
        self.label_titolo_login_2.grid(row=2, column=0, padx=(80, 20), pady=10, sticky="w")

        self.input_email = customtkinter.CTkEntry(self,
                                                   placeholder_text="Email",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_email.grid(row=3, column=0, padx=20, pady=(20,0))

        self.input_password = customtkinter.CTkEntry(self,
                                                   placeholder_text="Password",
                                                   show="*",
                                                   font=("Arial", 18),
                                                   corner_radius=10,
                                                   width=400,
                                                   height=50)
        self.input_password.grid(row=4, column=0, padx=20, pady=(20,0))

        self.label_linea_separazione = customtkinter.CTkLabel(self,
                                                              text="__________________________________________________________________",
                                                              font=("Arial", 10),
                                                              compound="left")
        self.label_linea_separazione.grid(row=5, column=0, padx=20, pady=20)

        self.pulsante_continua = customtkinter.CTkButton(self,
                                                         text="Continua",
                                                         font=("Arial", 20),
                                                         corner_radius=10,
                                                         width=400,
                                                         height=50,
                                                         command=self.login)
        self.pulsante_continua.grid(row=6, column=0, padx=20, pady=(10, 20))

        self.label_domanda_registrazione = customtkinter.CTkLabel(self,
                                                              text="Non hai un account?",
                                                              font=("Arial", 18),
                                                              compound="left")
        self.label_domanda_registrazione.grid(row=7, column=0, padx=20, pady=10)

        self.pulsante_registrati = customtkinter.CTkButton(self,
                                                         text="Registrati",
                                                         font=("Arial", 20),
                                                         corner_radius=10,
                                                         width=400,
                                                         height=50,
                                                         command=self.passaggio_signin)
        self.pulsante_registrati.grid(row=8, column=0, padx=20, pady=(0, 20))

    def login(self):
        email = self.input_email.get()
        password = self.input_password.get()

        if self.database.login(email, password):
            self.open_main_app(self.database.login(email, password))

    def passaggio_signin(self):
        from views.signin import App_Finestra_Signin
        self.destroy()

        self.master.title("CoreCapital - Signin")
        self.master.geometry("1000x900")
        self.master.resizable(False, False)

        self.finestra_signin = App_Finestra_Signin(self.master, self.database)
        self.finestra_signin.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def open_main_app(self, sessione_utente):
        from views.main_app import MainApp
        self.destroy()

        self.master.geometry("1400x900")
        self.master.title("CoreCapital")
        self.master.resizable(True, True)

        self.sessione_utente = sessione_utente

        self.main_app = MainApp(self.master, self.database, self.sessione_utente)
        self.main_app.grid(row=0, column=0, sticky="nsew")