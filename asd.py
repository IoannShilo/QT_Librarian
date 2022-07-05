import pypyodbc
from faker import Faker
from random import randint


fake = Faker()

connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=vpngw.avalon.ru;'
                                      'Database=DevDB2022_IVASHI;'
                                      'uid=tsqllogin;'
                                      'pwd=Pa$$w0rd;')
cursor = connection.cursor()
mySQLQuery = ("""INSERT INTO Library.Book_copy (Book_copy_id, ISBN, issued_not_issued)

                            VALUES (N'%s', N'%s', N'%s')""" % (randint(000000, 999999), '978-0-619-59725-2', 'не выдан'))





cursor.execute(mySQLQuery)
cursor.commit()
