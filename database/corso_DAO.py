# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from database.DB_connect import DBconnect

class DAO():
    @staticmethod
    def getAllCorsi():
        cnx = DBconnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * FROM corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

    def getCorsiMatricola(matricola):
        cnx = DBconnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.*
                from corso c, studente s,iscrizione i
                where s.matricola=i.matricola and i.codins =c.codins and s.matricola =%s"""
        cursor.execute(query,(matricola,))

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorso(codins):
       cnx = DBconnect.get_connection()
       cursor = cnx.cursor(dictionary=True)
       query = """select c.*
                    from corso c
                    where c.codins=%s  """
       cursor.execute(query, (codins,))

       row = cursor.fetchone()
       if row is not None:
           res = (Corso(
               codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]

           ))

           cursor.close()
           cnx.close()
           return res


