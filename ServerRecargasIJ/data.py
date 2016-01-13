import sqlite3
import sys
import json   
import responses
    
def open_connection():
    connection = sqlite3.connect('Recargas.db3')
    connection.row_factory = dict_factory
    return connection

def get_json_data(query):
    try:
        connection = open_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return json.dumps(data)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    
def insert_json_data(insert_query, insert_data):
    try:
        connection = sqlite3.connect('Recargas.db3')
        cursor = connection.cursor()
        cursor.execute(insert_query, insert_data)
        connection.commit()
        connection.close()
        return responses.get_json_status({'success':True}, 200)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        return responses.get_json_status({'success':False}, 500)
        raise
    
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d