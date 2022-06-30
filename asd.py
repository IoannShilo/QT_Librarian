import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=vpngw.avalon.ru;'
                                      'Database=DevDB2022_IVASHI;'
                                      'uid=tsqllogin;'
                                      'pwd=Pa$$w0rd;')
cursor = connection.cursor()
mySQLQuery = ("""
                SELECT *
                FROM Library.Readers
                """)
cursor.execute(mySQLQuery)
results = cursor.fetchall()
print(results)