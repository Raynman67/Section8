# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:38:40 2021

@author: raymo
"""

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query="INSERT INTO users VALUES(?, ?, ?) "
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')    
    ]

cursor.executemany(insert_query, users)


select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()