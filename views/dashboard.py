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

class Frame_Conto(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database
        

class Frame_Dashboard_Content(customtkinter.CTkScrollableFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=0, minsize=150)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.frame_conto1 = Frame_Conto(self, self.database)
        self.frame_conto1.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        self.frame_conto2 = Frame_Conto(self, self.database)
        self.frame_conto2.grid(row=0, column=1, padx=10, pady=(20, 10), sticky="nsew")

        self.frame_conto3 = Frame_Conto(self, self.database)
        self.frame_conto3.grid(row=0, column=2, padx=(10, 20), pady=(20, 10), sticky="nsew")

        self.frame_piechart = Frame_PieChart(self, self.database)
        self.frame_piechart.grid(row=1, column=0, rowspan=2, columnspan=2, padx=(20, 10), pady=10, sticky="nsew")

        self.frame_ultima_attività = Frame_Ultima_Attività(self, self.database)
        self.frame_ultima_attività.grid(row=1, column=2, padx=(10, 20), pady=10, sticky="nsew")

        self.frame_avvisi = Frame_Avvisi(self, self.database)
        self.frame_avvisi.grid(row=2, column=2, padx=(10, 20), pady=10, sticky="nsew")

        self.frame_cronologia = Frame_Cronologia(self, self.database)
        self.frame_cronologia.grid(row=3, column=0, columnspan=3, padx=20, pady=(10, 20), sticky="nsew")



        

class Dashboard(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master, corner_radius=0)
        self.database = database

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0, minsize=50)
        self.rowconfigure(1, weight=1)

        self.label_titolo = customtkinter.CTkLabel(self,
                                                   text="Dashboard",
                                                   font=("Arial", 30, "bold"),
                                                   compound="left")
        self.label_titolo.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="nsw")

        self.frame_dashboard_content = Frame_Dashboard_Content(self, self.database)
        self.frame_dashboard_content.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="nsew")
