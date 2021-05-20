# -*- coding: utf-8 -*-
"""
Created on Wed May 19 09:59:44 2021

@author: raymo
"""
import sqlite3
from db import db

class UserModel(db.Model):
    
    __table__name = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    # Initialze a User obj
    def __init__(self, username, password):
        self.username = username
        self.password = password
   
    """
    does both insert and update
    """
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    """
    deletes from db
    """    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    # find a user by name from  users table in data.db
    @classmethod
    def find_by_username(cls, username):            
        return cls.query.filter_by(username=username).first() # select * from users where name={name} limit 1


    # find a user by ID from  users table in data.db
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() # select * from users where id={_id} limit 1