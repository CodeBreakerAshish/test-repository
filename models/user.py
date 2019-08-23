from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self,username,password):
        self.username = username
        self.password = password


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getuser_byname(cls,username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def getuser_byid(cls,_id):
        return cls.query.filter_by(id=_id).first()
