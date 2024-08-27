from utils import database
from typing import Dict

class Cimcnd():
    conn_origin = database.Connections().connection_CIMCND()
    def get_all_records(self):
        # use origin connection
        SQL_QUERY = "SELECT * FROM Transactions"

        cursor = self.conn_origin.cursor()
        cursor.execute(SQL_QUERY)

        print("Results from ORIGIN")

        
        for r in cursor.fetchall():
            yield {
                "id": r[0],
                "name": r[1],
                "hash": r[2],
                "currency": r[3],
                "execution_hour": r[4],
                "type": r[5],
                "state": r[6]
            }