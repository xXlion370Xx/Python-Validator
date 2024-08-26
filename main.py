from utils import database

conn = database.Connections().connection_CIMCND()

# Usar la conexión
SQL_QUERY = """
SELECT * FROM Transactions
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)

for r in cursor.fetchall():
    print(r)


