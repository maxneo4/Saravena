import sqlite3
import sys
   
def get_users():
    try:
        conn = sqlite3.connect('Recargas.db3')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Cliente')   
        data = cursor.fetchall()
        conn.close()
        return data
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d