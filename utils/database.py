import pyodbc
import os 
from dotenv import load_dotenv

load_dotenv()
SERVER = os.getenv('SERVER')
DATABASE= os.getenv('DATABASE')
USERNAME= os.getenv('US')
PASSWORD= os.getenv('PASSWORD')
TRUSTED_CONN = "Yes"


class Connections():
    
    connectionString = f'Trusted_Connection={TRUSTED_CONN};DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

    def connection_CIMCND(self):
        try:
            print("Connecting database CIMCND")
            conn = pyodbc.connect(self.connectionString)
            
            return conn

        except pyodbc.Error as e:
            print("Something went wrong during database connection")
            print(e)