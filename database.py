import sqlite3

class Database:
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def login(self, email, password):
        self.email = email
        self.password = password

        self.cursor.execute("""SELECT *
                            FROM Utente
                            WHERE Email = ? AND Password = ?""",
                            (self.email, self.password))
        utente = self.cursor.fetchone()

        return utente
        
    def signin(self, codicefiscale, email, password, cognome, nome, cittànascita, datanascita, residenza, cittadinanza, numerocellulare):
        self.codicefiscale = codicefiscale
        self.email = email
        self.password = password
        self.cognome = cognome
        self.nome = nome
        self.cittànascita = cittànascita
        self.datanascita = datanascita
        self.residenza = residenza
        self.cittadinanza = cittadinanza
        self.numerocellulare = numerocellulare

        self.cursor.execute("""INSERT INTO Utente 
                            (CodiceFiscale, Email, Password, Cognome, Nome, CittàNascita, DataNascita, Residenza, Cittadinanza, NumeroCellulare)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                            (self.codicefiscale, self.email, self.password, self.cognome, self.nome, self.cittànascita, self.datanascita, self.residenza, self.cittadinanza, self.numerocellulare))
        self.conn.commit()