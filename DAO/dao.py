import mysql.connector


class DAO:

    def getAllProdotti(self)
    #connection
        cnx: mysql.connector.connect(
            user= "root",
            password = "root",
            host = "localhost",
            database = "sw_gestionale",
        )
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM prodotti")
    prodotti= cursor.fetchall()
    for p in prodotti:
        print(p)
    cursor.close()
    cnx.close()
    return

if __name__ == "__main__":
    mydao= DAO()
    mydao.getAllProdotti()


