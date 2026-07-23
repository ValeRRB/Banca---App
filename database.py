import sqlite3
from faker import Faker
import datetime

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

    def creaConto(self, codicefiscale, saldo=0, tipoconto="Standard", statoconto="Attivo"):
        self.codicefiscale = codicefiscale
        fake = Faker("it_IT")
        self.IBAN = fake.iban()
        self.saldo = saldo
        self.tipoConto = tipoconto
        self.dataApertura = datetime.date.today()
        self.statoconto = statoconto

        self.cursor.execute("""INSERT INTO Conto
                            (IBAN, Saldo, TipoConto, DataApertura, StatoConto, Proprietario)
                            VALUES (?, ?, ?, ?, ?, ?)""",
                            (self.IBAN, self.saldo, self.tipoConto, self.dataApertura, self.statoconto, self.codicefiscale))
        
        self.conn.commit()

    def getContiUtente(self, codicefiscale):
        self.codicefiscale = codicefiscale
        self.cursor.execute("""SELECT IBAN, Saldo, TipoConto, StatoConto
                            FROM Conto WHERE Proprietario = ?""", (self.codicefiscale,))
        return self.cursor.fetchall()

    def getCodiceFiscaleByEmail(self, email):
        self.email = email
        self.cursor.execute("""SELECT CodiceFiscale
                            FROM Utente WHERE EMail == ?""", (self.email,))
        self.risultato = self.cursor.fetchone()
        if self.risultato:
            return self.risultato[0]
        return None