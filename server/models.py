from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import bcrypt, db


class User(db.Model) :
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'