import customtkinter
from tkinter import TclError
from PIL import Image
import os, sys

# ============== CHATGPT - PATH ASSOLUTO DI UN ELEMENTO ==============
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# ====================================================================

class ContoBancario:
    def __init__(self, saldo, lista_operazioni, lista_denaro):
        self.saldo = saldo
        self.lista_operazioni = lista_operazioni
        self.lista_denaro = lista_denaro
    
    def deposita(self, denaro):
        self.saldo += denaro
    
    def preleva(self, denaro):
        if denaro <= self.saldo:
            self.saldo -= denaro

class Frame_Saldo(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=24)

        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        self.label_saldo = customtkinter.CTkLabel(self, 
                                                  text="Saldo:", 
                                                  font=("Arial", 20, "bold"), 
                                                  fg_color="transparent", 
                                                  anchor="w")
        self.label_saldo.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        self.label_valore_saldo = customtkinter.CTkLabel(self, 
                                                         text="€"+"0,00"+" EUR", 
                                                         font=("Arial", 48), 
                                                         fg_color="transparent", 
                                                         anchor="w")
        self.label_valore_saldo.grid(row=1, column=0, padx=20, sticky="w")

        self.label_disponibile = customtkinter.CTkLabel(self, 
                                                        text="disponibile",
                                                        font=("Arial", 18), 
                                                        fg_color="transparent",
                                                        anchor="w")
        self.label_disponibile.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")

class Frame_Utente(customtkinter.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master, corner_radius=24)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)

        self.profilo_utente_icona = customtkinter.CTkImage(Image.open(resource_path(r"assets\user.png")),
                                                           size=(80, 80))
        self.profilo_utente_icona_label = customtkinter.CTkLabel(self,
                                                                 image=self.profilo_utente_icona,
                                                                 text=None)
        self.profilo_utente_icona_label.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

        self.profilo_utente_label_username = customtkinter.CTkLabel(self,
                                                                   text=username,
                                                                   font=("Arial", 18), 
                                                                   fg_color="transparent")
        self.profilo_utente_label_username.grid(row=0, column=1, padx=20, sticky="s")

        self.pulsante_impostazioni = customtkinter.CTkButton(self,
                                                             text="Informazioni App",
                                                             font=("Arial", 18),
                                                             corner_radius=24,
                                                             width=200,
                                                             height=40,
                                                             command=self.visualizza_informazioni)
        self.pulsante_impostazioni.grid(row=1, column=1, padx=20)

    def visualizza_informazioni(self):
        self.impostazioni = Input_informazioni(self)
        self.impostazioni.attesa_input()

class Input_informazioni(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Conto Bancario - Informazioni")
        self.geometry("500x650")
        self.resizable(False, False)

        self.grab_set()
        self.focus_force()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)

        self.label_titolo = customtkinter.CTkLabel(self,
                                                    text=("Informazioni - Versione 0.3.0\n"
                                                          "__________________________________________________________________"),
                                                    font=("Arial", 34),
                                                    fg_color="transparent")
        self.label_titolo.grid(row=0, column=0, padx=20, pady=(20, 0))

        self.label_testo1 = customtkinter.CTkLabel(self,
                                                  text=("App realizzata su Visual Studio Code principalmente con\n"
                                                        "le seguenti librerie:\n"
                                                        "\n"
                                                        "• CustomTkinter - [UI & App vera e propria]\n"
                                                        "• Pillow (PIL) - [per immagini]\n"
                                                        "• altre (os, sys, tkinter)\n"
                                                        "\n"
                                                        "__________________________________________________________________"),
                                                        font=("Arial", 18),
                                                        fg_color="transparent",
                                                        justify="center")
        self.label_testo1.grid(row=1, column=0, padx=20, pady=(20, 0))



        self.label_testo2 = customtkinter.CTkLabel(self,
                                                  text=("Per trasformare il codice in un file .exe è stato utilizzato:\n"
                                                        "\n"
                                                        "• Pyinstaller (tramite un comando nel terminale)\n"
                                                        "\n"
                                                        "__________________________________________________________________"),
                                                        font=("Arial", 18),
                                                        fg_color="transparent",
                                                        justify="center")
        self.label_testo2.grid(row=2, column=0, padx=20, pady=(20, 0))

        self.label_testo3 = customtkinter.CTkLabel(self,
                                                  text=("Per ottenere il file setup è stata utilizzata la seguente app:\n"
                                                        "\n"
                                                        "• Inno Setup Compiler\n"),
                                                        font=("Arial", 18),
                                                        fg_color="transparent",
                                                        justify="center")
        self.label_testo3.grid(row=3, column=0, padx=20, pady=(20, 0))


        self.pulsante_continua = customtkinter.CTkButton(self,
                                                         text="Continua",
                                                         font=("Arial", 18),
                                                         corner_radius=24,
                                                         width=340,
                                                         height=40,
                                                         command=self.Input_continua)
        self.pulsante_continua.grid(row=4, column=0, sticky="s", padx=30, pady=(30, 20))

        self.focus_force()

    def Input_continua(self):
        self.destroy()

    def attesa_input(self):
        self.wait_window()

class Frame_Azioni(customtkinter.CTkFrame):
    def __init__(self, master, username, framesaldo, conto_utente, frameregistro):
        super().__init__(master, corner_radius=24)
        self.conto_utente = conto_utente
        self.framesaldo = framesaldo
        self.frameregistro = frameregistro

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        self.pulsante_aggiungi_denaro = customtkinter.CTkButton(self,
                                                                text="Aggiungi Denaro",
                                                                font=("Arial", 18),
                                                                corner_radius=24,
                                                                width=340,
                                                                height=40,
                                                                command=self.Aggiungi_Denaro)
        self.pulsante_aggiungi_denaro.grid(row=0, column=0, padx=20, pady=(10, 0))

        self.pulsante_preleva_denaro = customtkinter.CTkButton(self,
                                                                text="Preleva Denaro",
                                                                font=("Arial", 18),
                                                                corner_radius=24,
                                                                width=340,
                                                                height=40,
                                                                command=self.Preleva_Denaro)
        self.pulsante_preleva_denaro.grid(row=1, column=0, padx=20, pady=(10, 0))
        
        self.tema_app_impostazione = customtkinter.CTkSwitch(self,
                                                             text="Tema App - Chiaro/Scuro",
                                                             font=("Arial", 18),
                                                             command=self.Switch_Tema)
        self.tema_app_impostazione.grid(row=2, column=0, sticky="sew", padx=20, pady=(0, 10))

        current_mode = customtkinter.get_appearance_mode().lower()
        if current_mode == "dark":
            self.tema_app_impostazione.select()
        else:
            self.tema_app_impostazione.deselect()

        self.Utente = Frame_Utente(self, username)
        self.Utente.grid(row=3, column=0, sticky="sew", padx=10, pady=(0, 10))
        
    def Aggiungi_Denaro(self):
        self.finestra_aggiunta_denaro = Input_Aggiungi_Denaro(self)
        self.denaro = float(self.finestra_aggiunta_denaro.attesa_input())
        if not self.denaro:
            self.master.destroy()
        else:
            self.conto_utente.deposita(self.denaro)
            self.framesaldo.label_valore_saldo.configure(text=f"€{self.conto_utente.saldo:.2f} EUR")
            self.conto_utente.lista_operazioni.append("positivo")
            self.conto_utente.lista_denaro.append(self.denaro)
            self.frameregistro.aggiorna()

    def Preleva_Denaro(self):
        self.finestra_rimozione_denaro = Input_Aggiungi_Denaro(self)
        self.denaro = float(self.finestra_rimozione_denaro.attesa_input())
        if not self.denaro:
            self.master.destroy()
        else:
            self.conto_utente.preleva(self.denaro)
            self.framesaldo.label_valore_saldo.configure(text=f"€{self.conto_utente.saldo:.2f} EUR")
            self.conto_utente.lista_operazioni.append("negativo")
            self.conto_utente.lista_denaro.append(self.denaro)
            self.frameregistro.aggiorna()

    def Switch_Tema(self):
        if self.tema_app_impostazione.get() == 1:
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")

class Frame_Registro_Operazione(customtkinter.CTkFrame):
    def __init__(self, master, tipologia, denaro):
        super().__init__(master, corner_radius=24)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=0)

        if tipologia == "positivo":
            self.icona_operazione = customtkinter.CTkImage(Image.open(resource_path(r"assets\transaction_positive.png")),
                                                           size=(60, 60))
            self.label_icona_operazione = customtkinter.CTkLabel(self,
                                                                 image=self.icona_operazione,
                                                                 text=None)
            self.label_testo_operazione1 = customtkinter.CTkLabel(self,
                                                                 text=f"Aggiunto €{denaro:.2f} EUR",
                                                                 font=("Arial", 20))

        elif tipologia == "negativo":
            self.icona_operazione = customtkinter.CTkImage(Image.open(resource_path(r"assets\transaction_negative.png")),
                                                           size=(60, 60))
            self.label_icona_operazione = customtkinter.CTkLabel(self,
                                                                 image=self.icona_operazione,
                                                                 text=None)
            self.label_testo_operazione1 = customtkinter.CTkLabel(self,
                                                                 text=f"Rimosso €{denaro:.2f} EUR",
                                                                 font=("Arial", 20))

        self.label_testo_operazione2 = customtkinter.CTkLabel(self,
                                                                 text="Stato: successo ✅",
                                                                 font=("Arial", 20))

        self.label_icona_operazione.grid(row=0, column=0, padx=10, pady=10)
        self.label_testo_operazione1.grid(row=0, column=1, sticky="w", padx=0, pady=10)
        self.label_testo_operazione2.grid(row=0, column=2, sticky="e", padx=20, pady=10)

class Frame_Registro(customtkinter.CTkScrollableFrame):
    def __init__(self, master, conto_utente):
        super().__init__(master, corner_radius=24)
        self.columnconfigure(0, weight=1)
        self.conto_utente = conto_utente

        self.label_titolo = customtkinter.CTkLabel(self,
                                                    text=("Registro"),
                                                    font=("Arial", 24, "bold"),
                                                    fg_color="transparent")
        self.label_titolo.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 20))

        self.frames_operazioni = []

    def aggiorna(self):
        for frame in self.frames_operazioni:
            frame.destroy()
        self.frames_operazioni.clear()

        for fila, operazione in enumerate(self.conto_utente.lista_operazioni):
            denaro = self.conto_utente.lista_denaro[fila]
            frame_operazione = Frame_Registro_Operazione(self, operazione, denaro)
            frame_operazione.grid(row=fila+1, column=0, sticky="ew", padx=(0, 10), pady=(0, 10))
            self.frames_operazioni.append(frame_operazione)
   
class Input_Aggiungi_Denaro(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Conto Bancario - Input")
        self.geometry("400x180")
        self.resizable(False, False)

        self.grab_set()
        self.focus_force()

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        self.label_input = customtkinter.CTkLabel(self, 
                                                  text="Inserire somma di denaro",
                                                  font=("Arial", 18), 
                                                  fg_color="transparent")
        self.label_input.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,0))

        self.input_utente = customtkinter.CTkEntry(self,
                                                   placeholder_text="Denaro",
                                                   font=("Arial", 14),
                                                   corner_radius=24,
                                                   width=250)
        self.input_utente.grid(row=1, column=0, columnspan=2, padx=20, pady=(20,0))

        self.pulsante_continua = customtkinter.CTkButton(self,
                                                         text="Continua",
                                                         font=("Arial", 18),
                                                         corner_radius=24,
                                                         width=170,
                                                         height=40,
                                                         command=self.Input_continua)
        self.pulsante_continua.grid(row=2, column=0, sticky="s", padx=(20, 10), pady=(20,0))

        self.pulsante_annulla = customtkinter.CTkButton(self,
                                                         text="Annulla",
                                                         font=("Arial", 18),
                                                         corner_radius=24,
                                                         width=170,
                                                         height=40,
                                                         command=self.Input_annulla)
        self.pulsante_annulla.grid(row=2, column=1, sticky="s", padx=(10, 20), pady=(20,0))

        self.focus_force()
        self.denaro = None

    def Input_continua(self):
        self.denaro = self.input_utente.get()
        self.destroy()

    def Input_annulla(self):
        self.denaro = None
        self.destroy()

    def attesa_input(self):
        self.wait_window()
        return self.denaro

class Input_Username(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Conto Bancario - Login")
        self.geometry("450x300")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)

        self.profilo_utente_icona = customtkinter.CTkImage(Image.open(resource_path(r"assets\user.png")),
                                                           size=(60, 60))
        self.profilo_utente_icona_label = customtkinter.CTkLabel(self,
                                                                 image=self.profilo_utente_icona,
                                                                 text=None,
                                                                 compound="center")
        self.profilo_utente_icona_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0))

        self.label_input = customtkinter.CTkLabel(self, 
                                                  text="User Login",
                                                  font=("Arial", 34), 
                                                  fg_color="transparent")
        self.label_input.grid(row=1, column=0, columnspan=2, padx=20, pady=(20,0))

        self.input_utente = customtkinter.CTkEntry(self,
                                                   placeholder_text="Nome utente",
                                                   font=("Arial", 14),
                                                   corner_radius=24,
                                                   width=250)
        self.input_utente.grid(row=2, column=0, columnspan=2, padx=20, pady=(20,0))

        self.pulsante_continua = customtkinter.CTkButton(self,
                                                         text="Continua",
                                                         font=("Arial", 18),
                                                         corner_radius=24,
                                                         width=170,
                                                         height=40,
                                                         command=self.Input_continua)
        self.pulsante_continua.grid(row=3, column=0, sticky="s", padx=(20, 0), pady=(20,0))

        self.pulsante_annulla = customtkinter.CTkButton(self,
                                                         text="Annulla",
                                                         font=("Arial", 18),
                                                         corner_radius=24,
                                                         width=170,
                                                         height=40,
                                                         command=self.Input_annulla)
        self.pulsante_annulla.grid(row=3, column=1, sticky="s", padx=(0, 20), pady=(20,0))

        self.focus_force()
        self.username = None

    def Input_continua(self):
        self.username = self.input_utente.get()
        self.destroy()

    def Input_annulla(self):
        self.username = None
        self.destroy()

    def attesa_input(self):
        self.wait_window()
        return self.username        

class Frame_App(customtkinter.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master, corner_radius=0)
        self.username = username
        self.lista_operazioni = []
        self.lista_denaro = []
        self.conto_utente = ContoBancario(0.00, self.lista_operazioni, self.lista_denaro)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=4)

        self.FrameSaldo = Frame_Saldo(self)
        self.FrameSaldo.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        self.FrameRegistro = Frame_Registro(self, self.conto_utente)
        self.FrameRegistro.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(5, 10), pady=10)

        self.FrameAzioni = Frame_Azioni(self, self.username, self.FrameSaldo, self.conto_utente, self.FrameRegistro)
        self.FrameAzioni.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Conto Bancario")
        self.geometry("1200x800")
        self.resizable(False, False)

        customtkinter.set_default_color_theme("green")
        customtkinter.set_appearance_mode("dark")

        self.login_input = Input_Username(self)
        self.username = self.login_input.attesa_input()

        if not self.username:
            self.destroy()
        else:
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.UI = Frame_App(self, self.username)
            self.UI.grid(row=0, column=0, sticky="nsew")

app = App()
# Only start mainloop if the root window still exists
try:
    app.mainloop()
except TclError:
    pass