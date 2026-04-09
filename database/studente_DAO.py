# Add whatever it is needed to interface with the DB Table studente
import mysql

from database.DB_connect import DBconnect
from model.studente import Studente

class DAO():
    @staticmethod
    def getStudentiCorso(codice_corso):
        cnx = DBconnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.*
                from iscrizione i,corso c ,studente s
                where  i.matricola = s.matricola  and c.codins=i.codins  and c.codins =%s """
        cursor.execute(query,(codice_corso,))

        res = []
        for row in cursor:
            res.append(Studente(
                nome=row["nome"],
                cognome=row["cognome"],
                matricola=row["matricola"],
                cds=row["CDS"]
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudenteMatricola(matricola):
        cnx = DBconnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.*
                       from studente s
                       where s.matricola =%s """
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        if row is not None:
            res=(Studente(
                    nome=row["nome"],
                    cognome=row["cognome"],
                    matricola=row["matricola"],
                    cds=row["CDS"]
                ))

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def creaIscrizione(codins,matricola):
        try:
            cnx = DBconnect.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """insert into iscrizione (codins,matricola)
                        values(%s,%s) """
            cursor.execute(query, (codins,matricola,))

            cnx.commit()

            cursor.close()
            cnx.close()
            return True

        except mysql.connector.IntegrityError:
            # Questo intercetta specificamente il "Duplicate entry"
            print("Lo studente è già iscritto a questo corso.")
            return False



