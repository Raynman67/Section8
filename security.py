# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:47:56 2021

@author: raymo
"""
from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user =UserModel.find_by_username(username)   #username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)