from models.user import UserModel


def authenticate(username,password):
    user = UserModel.getuser_byname(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.getuser_byid(user_id)
