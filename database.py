import sqlite3
from json import dumps
import time
#con=sqlite3.connect('connect_data.db')
#c=con.cursor()
#table name trafficdata
#table creation

#c.execute("DROP TABLE trafficdata")
#con.commit()
'''
c.execute("""CREATE TABLE traffic (
    date_1 text,
    lane_name integer,
    lane integer,
    time1 real
)
""")
'''

def insert_data(l1,lane_name):
    con=sqlite3.connect('connect_data.db')
    c=con.cursor()
    localtime = time.asctime( time.localtime(time.time()))
    jsonarray = dumps(l1[:5])
    c.execute("INSERT INTO traffic (date_1,lane_name,lane,time1) VALUES (?,?,?,?)",(localtime,int(lane_name),jsonarray,l1[5]))
    con.commit()
    con.close()



#'''
def printall():
    con=sqlite3.connect('connect_data.db')
    c=con.cursor()
    c.execute("SELECT * FROM traffic")
    items=c.fetchall()
    for item in items:
        print(item)
    con.commit()
    con.close()

#'''
#con.commit()
#con.close()