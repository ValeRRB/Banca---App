import customtkinter
from PIL import Image
from utils import resource_path

class Notifica_Creazione_Utente(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("CoreCapital - Creazione Conto")
        self.geometry("500x250")
        self.resizable(False, False)

        self.grab_set()
        self.focus_force()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.icona_login = customtkinter.CTkImage(Image.open(resource_path(r"assets\icon.ico")),
                                                                   size=(40, 40))
        self.label_icona_login = customtkinter.CTkLabel(self,
                                                        image=self.icona_login,
                                                        text=" CoreCapital Bank",
                                                        font=("Arial", 30, "bold"),
                                                        compound="left")
        self.label_icona_login.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30))

        self.check_success = customtkinter.CTkImage(Image.open(resource_path(r"assets/check.png")),
                                                    size=(40, 40))
        self.label_check_success = customtkinter.CTkLabel(self,
                                                          image=self.check_success,
                                                          text=None)
        self.label_check_success.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="nse")

        self.label_message = customtkinter.CTkLabel(self,
                                                    text="Utente creato con successo!",
                                                    font=("Arial", 24),
                                                    compound="left")
        self.label_message.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="nsew")

        self.pulsante_continua = customtkinter.CTkButton(self,
                                                         text="Continua",
                                                         font=("Arial", 20),
                                                         corner_radius=10,
                                                         width=400,
                                                         height=50,
                                                         command=self.chiudi_notifica)
        self.pulsante_continua.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    def chiudi_notifica(self):
        self.destroy()