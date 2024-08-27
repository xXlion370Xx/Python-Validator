import pyodbc
import os 
from dotenv import load_dotenv

load_dotenv()
SERVER = os.getenv('SERVER')
ORIGIN_DATABASE= os.getenv('ORIGIN_DATABASE')
DESTINE_DATABASE = os.getenv('DESTINE_DATABASE')
USERNAME= os.getenv('US')
PASSWORD= os.getenv('PASSWORD')
TRUSTED_CONN = "Yes"


class Connections():
    
    ## Origin
    def connection_CIMCND(self):
        connectionString = f'Trusted_Connection={TRUSTED_CONN};DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={ORIGIN_DATABASE};UID={USERNAME};PWD={PASSWORD}'
        try:
            print("Connecting database CIMCND")

            return pyodbc.connect(connectionString)
        
        except pyodbc.Error as e:
            print("Something went wrong during database connection")
            print(e)

    ##Destination
    def connection_Destino(self):
        connectionString = f'Trusted_Connection={TRUSTED_CONN};DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DESTINE_DATABASE};UID={USERNAME};PWD={PASSWORD}'
        try:
            print("Connecting database Destino")

            return pyodbc.connect(connectionString)
        
        except pyodbc.Error as e:
            print("Something went wrong during database connection")
            print(e)
