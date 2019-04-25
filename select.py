#!/usr/bin/env python

import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('SELECT * from test-table')
print c.fetchall()

conn.close()
