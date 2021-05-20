# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:56:56 2021

@author: raymo
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
                        type=float,
                        required = True,
                        help='This feild cannot be left blank')
    
    parser.add_argument('store_id', 
                        type=int,
                        required = True,
                        help='This feild is a foriegn key to stores table')
    
    @jwt_required()
    def get(self, name):
        
        item =ItemModel.find_by_name(name)
        if item:
            return item.json()
       
        #implicit else
        return{'message': 'items {} not found'.format(name)},404
        
    def post(self, name):
        
        if  ItemModel.find_by_name(name):
            return{'message': 'Item with name {} already exists'.format(name)}, 400
            
        request_data = Item.parser.parse_args()
        
        item = ItemModel( name, request_data['price'], request_data['store_id'])
        
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting item "}, 500 #internal server error
        
        return item.json(), 201
        
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            
        return{'message': 'item {} deleted'.format(name)}
    
    def put(self, name):
        # some comment to edit fn  
        request_data =Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name, request_data['price'], request_data['store_id'])
        else :
            item.price = request_data['price']
            item.store_id = request_data['store_id']
         
        item.save_to_db()
        return item.json()  
    
  
class ItemList(Resource):
    
    def get(self):
        return{'items': [item.json for item in ItemModel.query.all()] }