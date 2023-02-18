#import sqlite3
import pyodbc as pyodbc


class Connector:
    def __init__(self, database_url):
        #conn = sqlite3.connect(database_url)
        conn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=TRN;Trusted_Connection=yes;')
        self.cursor = conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def execute_sql(self, schema, table):
        sql="select distinct table_schema, table_name from information_schema.tables where table_schema like '"+schema+"' and table_name like '"+table+"'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
