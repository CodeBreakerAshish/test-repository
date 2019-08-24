import os
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegsiter
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ASHISH'
api  = Api(app)



jwt  = JWT(app, authenticate, identity) #/auth



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegsiter, '/register')
api.add_resource(Store  ,'/store/<string:name>')
api.add_resource(StoreList  ,'/stores')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True )
