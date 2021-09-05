import os
import random
import string
import json
import sqlite3

conn = sqlite3.connect('dummydata.db')

cur = conn.cursor()

conn.execute('''

CREATE TABLE Customers(
   CustID INTEGER PRIMARY KEY AUTOINCREMENT,
   FirstName           TEXT      NOT NULL,
   LastName            INT       NOT NULL,
   Email        CHAR(75),
   Addr1        CHAR(50),
   Addr2        CHAR(50),
   Addr3        CHAR(50),
   Postcode     CHAR(50),
   TelNo        CHAR(50),
   Notes        CHAR(100),
   Active       INT
   ); ''')

conn.commit()
print('created table')
