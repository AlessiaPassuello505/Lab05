from database.corso_DAO import DAO as CorsoDAO
from database.studente_DAO import DAO as StudenteDAO

class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return CorsoDAO.getAllCorsi()

    def getStudentiCorso(self,codice_corso):
        return StudenteDAO.getStudentiCorso(codice_corso)

    def getStudenteMatricola(self,matricola):
        return StudenteDAO.getStudenteMatricola(matricola)

    def getCorsiMatricola(self,matricola):
        return CorsoDAO.getCorsiMatricola(matricola)

    def creaIscrizione(self,corso,matricola):
        return StudenteDAO.creaIscrizione(corso,matricola)

    def getCorso(self,codins):
        return CorsoDAO.getCorso(codins)