# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:16:27 2021

@author: raymo
"""

import sqlite3

connection=sqlite3.connect('data.db')
cursor = connection.cursor()

# MUST use INTEGER not int when creating auto-increment PK
create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text )"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items( id INTEGER PRIMARY KEY, name text, price real )"
cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES('test', 0.99)")

connection.commit()
connection.close()
