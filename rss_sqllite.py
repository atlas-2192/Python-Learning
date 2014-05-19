#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
rss_data
-rss_name
-link
-title
-etag
-modifired 

rss_item_(rss_name)
-item_index
_title
_link
_description
'''

def create_db(name, table_template):

def add_to_DB(insert_data):

def query_from_db(rss_data):

con = None

try:
    con = lite.connect('test2.db')
    with con:
        cur = con.cursor()    
        #cur.execute("DROP TABLE IF EXISTS Cars")
        #cur.execute("SELECT * FROM Cars")
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        t = ('cars',)
        cur.executemany("INSERT INTO Cars VALUES(? , ?, ?)", cars)
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print row
    cur = con.cursor()    

    '''
    fetch data at once
    '''
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data     


    print '----------------------------'
    '''
    fetch at one by one
    '''           
    cur.execute("SELECT * FROM Cars")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print row
    

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()


if __name__ == "__main__":        