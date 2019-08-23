from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.item import ItemModel




class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type = float, required = True,help = 'This Field can\'t be blank')
    parser.add_argument('store_id', type = int, required = True,help = 'All items have a store')




    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404







    def post(self,name):

        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already Exists.".format(name)} , 404
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message': "An error occured"} , 500

        return item.json() , 201



    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db
        return {'message':'Item deleted'}


        return {'messgae': 'Item deleted'}

    def put(self,name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)


        if item is None:
            item = ItemModel(name,data['price'], data['store_id'])
        else:
            item.price = data['price']

        return item.json()


        return updated_item.json()







class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
