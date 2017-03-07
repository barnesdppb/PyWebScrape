# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:26:21 2017

@author: dabarnes
"""

import pymysql

conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', passwd = 'the2Lora', db = 'mysql')

dct = {"title":"test insert", "content":"test content"}

cur = conn.cursor()
cur.execute("USE scraping")

for d in dct:
    cur.execute("INSERT INTO pages ({}) values (\"{}\")".format(d, dct[d]))
    cur.connection.commit()
#cur.execute("SELECT * from scraping.pages")
#out = cur.fetchone()
#print(cur.fetchone())
cur.close()
conn.close()



#-----------------------------------------------------------------------------#
# -------------- Insert values from dict into a MySQL database ---------------#
conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', passwd = 'the2Lora', db = 'mysql')

dct = {"title":"test insert", "content":"test content"}
placeholders = ', '.join(['%s'] * len(dct))
columns = ', '.join(dct.keys())

cur = conn.cursor()
cur.execute("USE scraping")

sql = "insert into pages (%s) values (%s)" % (columns, placeholders)
cur.execute(sql, list(dct.values()))