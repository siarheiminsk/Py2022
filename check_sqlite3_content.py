import pyodbc

with pyodbc.connect('DRIVER={SQLite3 ODBC Driver};Direct=True;'
                    'Database=content.db;StringTypes=Unicode') as connection:
    cursor = connection.cursor()
    cursor.execute('select * from forecasts')
    result = cursor.fetchall()
    print(result)
    cursor.close()