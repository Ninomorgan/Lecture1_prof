import mysql.connector
import pathlib


class DBConnect:
    myPool= None

    def __init__(self):
        #impedisce al chiamante di ccreare un istanza
        #implementiamo il pattern singletone
        raise RuntimeError("NON DEVI CREARE UN ISTANZA DI QUESTA CLASSE")

    @classmethod
    def getConnection(cls):
        if cls.myPool is None: #verifichiamo se già siste pool
            try:
                cnx= mysql.connector.connect(
                    user= "root",
                    passwd= "rootroot",
                    host= "localhost",
                    database= "sw_gestionale",
                    option_files= f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                cls.myPool= mysql.connector.pooling.MySQLConnectionPool(
                    user= "root",
                    passwd= "rootroot",
                    host= "localhost",
                    database= "sw_gestionale",
                    pool_size= 10,
                    pool_name= "myPool"

                )
                return cls.myPool.get_connection()
            except mysql.connector.Error as error:
                print(error)
        else:
            # esiste già connesisone
            return cls.myPool.get_connection()