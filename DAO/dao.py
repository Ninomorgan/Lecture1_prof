import mysql.connector

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.provaCollections import cliente


class DAO:

    def getAllProdotti(self):
        #connection
        cnx= mysql.connector.connect(
            user= "root",
            password = "rootroot",
            host = "localhost",
            database = "sw_gestionale",
        )
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prodotti")
        row= cursor.fetchall() #lista dizionari- righe che leggeiamo

        #creiamo degli oggetti di tipo Prodotto
        res= []
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"])) #p["nome"] è il nome che abbiamo associaaoto al databare
        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        # connection
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="localhost",
            database="sw_gestionale",
        )
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clienti")
        row = cursor.fetchall()  # lista dizionari- righe che leggeiamo

        # creiamo degli oggetti di tipo Prodotto
        res = []
        for c in row:
            res.append(ClienteRecord(c["nome"], c["mail"], c["categoria"]))  # p["nome"] è il nome che abbiamo associaaoto al databare
        cursor.close()
        cnx.close()
        return res


    #AGGIUNGIAMO
    def _addProdotto(self, prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="localhost",
            database="sw_gestionale",
        )
        cursor = cnx.cursor()
        query = "INSERT INTO prodotto (nome, prezzo) VALUES (%s, %s)"
        cursor.execute(query, (prodotto["nome"], prodotto["prezzo"]))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def addCliente(self, prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="localhost",
            database="sw_gestionale",
        )
        cursor = cnx.cursor()
        query = "INSERT INTO cliente (nome, mail, categoria) VALUES (%s, %s, %s)"
        cursor.execute(query, (cliente.nome, cliente.email, cliente.categoria))
        cnx.commit()
        cursor.close()
        cnx.close()
        return


if __name__ == "__main__":
    mydao= DAO()
    mydao.getAllProdotti()


