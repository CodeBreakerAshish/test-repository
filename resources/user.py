import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegsiter(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field cannot be blank"


    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
)



    def post(self):
        data = UserRegsiter.parser.parse_args()

        if UserModel.getuser_byname(data['username']):
            return {'message': 'User Already exists'} ,  400

        user = UserModel(**data)
        user.save_to_db()
        return {'message' : 'USER CREATED!!'} , 201
