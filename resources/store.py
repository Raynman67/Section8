# -*- coding: utf-8 -*-
"""
Created on Thu May 20 07:49:26 2021

@author: raymo
"""

from flask_restful import Resource, reqparse
from models.store import StoreModel

from flask_jwt import jwt_required
from models.item import ItemModel

class Store(Resource):
    
    
    def get(self, name):
        # return a specific store
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return { 'message': "Store {} not found".format(name)}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return{'message': "Store '{}' already exists".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': "An error occurred while inserting store '{}'".format(name)}, 500
        
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
    
        return {'message': "Store '{}' has been deleted".format(name)}
    
class StoreList(Resource):
    
    def get(self):
        return{'stores': [store.json() for store in StoreModel.query.all()]}