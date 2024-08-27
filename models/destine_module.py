class Destine():
    # use destine connection
    conn_destine = database.Connections().connection_Destino()
    SQL_QUERY2 = """
    SELECT * FROM Transactions
    """
    cursor = conn_destine.cursor()
    cursor.execute(SQL_QUERY2)


    print("Results from Destine")

    for r in cursor.fetchall():
        print(r)