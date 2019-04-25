#!/usr/bin/env python

import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()

sites = [('https://www.bing.com', 'b'),
        ('https://www.yahoo.com', 'a')]

c.executemany('INSERT INTO test-table VALUES (?,?)', sites)
conn.commit()
conn.close()
