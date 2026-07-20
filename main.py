import customtkinter
from database import Database
from utils import resource_path
from views.login import Frame_Finestra_Login

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("CoreCapital - Login")
        self.geometry("600x750")
        self.resizable(False, False)

        self.database = Database(r"db\ContoBancarioDatabase.db")
        
        customtkinter.set_default_color_theme(r"themes\rime.json")
        customtkinter.set_appearance_mode("light")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.frame_finestra_login = Frame_Finestra_Login(self, self.database)
        self.frame_finestra_login.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.frame_finestra_login.grid_propagate(False)

if __name__ == "__main__":
    app = App()
    app.mainloop()