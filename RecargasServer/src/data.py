import sqlite3
   
def get_users():
    try:
        conn = sqlite3.connect('Recargas.db3')
        conn.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise