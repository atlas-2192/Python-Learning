#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)
con = None

try:
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()    
        #cur.execute("DROP TABLE IF EXISTS Cars")
        #cur.execute("SELECT * FROM Cars")
        #cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
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

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()