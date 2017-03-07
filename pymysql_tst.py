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



#-----------------------------------------------------------------------------#
# -------------------- Now deal with dict of dict values ---------------------#
conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', passwd = 'the2Lora', db = 'mysql')

dct = {"title":"test insert", 
       "content":{"name":"content", "value":"test content"}}

placeholders = ', '.join(['%s'] * len(dct))
columns = ', '.join(dct.keys())

vals = []
for d in dct:
    if type(dct[d]) is dict:
        vals.append(dct[d]['value'])
    else:
        vals.append(dct[d])

cur = conn.cursor()
cur.execute("USE scraping")


sql = "insert into pages (%s) values (%s)" % (columns, placeholders)
cur.execute(sql, vals)



#-----------------------------------------------------------------------------#
# -------------------------------- longer dict -------------------------------#

dct = {"id":"255103","url":"http://en.espn.co.uk/sport/rugby/player/255103.html"
       ,"name":"Joey Carbery","number":"15","position":"FB","captain":"False",
       "subbed":"False","homeAway":"home","subToolTip":"","eventTimes":{"1":["51'","54'"]},
       "onPitch":"True","wasActive":"True","tries":{"value":2,"name":"Tries"},
       "tryassists":{"value":"0","name":"Try Assists"},"points":{"value":"10","name":"Points"},
       "kicks":{"value":"6","name":"Kicks"},"passes":{"value":"11","name":"Passes"},
       "runs":{"value":"10","name":"Runs"},"metres":{"value":"90","name":"Metres Run"},
       "cleanbreaks":{"value":"3","name":"Clean Breaks"},"defendersbeaten":{"value":"1",
       "name":"Defenders Beaten"},"offload":{"value":"1","name":"Offload"},
       "lineoutwonsteal":{"value":"0","name":"Lineout Won Steal"},
       "turnoversconceded":{"value":"1","name":"Turnovers Conceded"},
       "tackles":{"value":"3","name":"Tackles"},"missedtackles":{"value":"0","name":"Missed Tackles"},
       "lineoutswon":{"value":"0","name":"Lineouts Won"},
       "penaltiesconceded":{"value":"0","name":"Penalties Conceded"},
       "yellowcards":{"value":"0","name":"Yellow Cards"},
       "redcards":{"value":"0","name":"Red Cards"},"penalties":{"value":"0","name":"penalties"},
       "penaltygoals":{"value":"0","name":"Penalty Goals"},
       "conversiongoals":{"value":"0","name":"Conversion Goals"},
       "dropgoalsconverted":{"value":"0","name":"Drop Goals Converted"}}


cols = list(dct.keys())
cols = list(filter(lambda c: c != 'eventTimes', cols))
cols = list(filter(lambda c: c != 'url', cols))


placeholders = ', '.join(['%s'] * len(cols))
columns = ', '.join(cols)

vals = []
for d in dct:
    if d in cols:
        if type(dct[d]) is dict:
            vals.append(dct[d]['value'])
        else:
            vals.append(dct[d])


sql = """create table r_stats(id bigint(7) not null
                            , name varchar(200)
                            , number varchar(10)
                            , position varchar(10)
                            , captain varchar(10)
                            , subbed varchar(10)
                            , homeAway varchar(10)
                            , subToolTip varchar(10)
                            , onPitch varchar(10)
                            , wasActive varchar(10)
                            , tries bigint(7)
                            , tryassists bigint(7)
                            , points bigint(7)
                            , kicks bigint(7)
                            , passes bigint(7)
                            , runs bigint(7)
                            , metres bigint(7)
                            , cleanbreaks bigint(7)
                            , defendersbeaten bigint(7)
                            , offload bigint(7)
                            , lineoutwonsteal bigint(7)
                            , turnoversconceded bigint(7)
                            , tackles bigint(7)
                            , missedtackles bigint(7)
                            , lineoutswon bigint(7)
                            , penaltiesconceded bigint(7)
                            , yellowcards bigint(7)
                            , redcards bigint(7)
                            , penalties bigint(7)
                            , penaltygoals bigint(7)
                            , conversiongoals bigint(7)
                            , dropgoalsconverted bigint(7)
                            , primary key(id));""".replace("\n", "")


conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', passwd = 'the2Lora', db = 'mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute(sql)

sql_update = "insert into r_stats (%s) values (%s)" % (columns, placeholders)
cur.execute(sql_update, vals)