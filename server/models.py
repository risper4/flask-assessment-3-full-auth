from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import bcrypt, db


class User(db.Model) :
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    @hybrid_property
    def password_hash(self) :
        raise AttributeError('Password hashes are not to be viewed')

    @password_hash.setter
    def password_hash(self, password) :
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password) :
        return bcrypt.check_password_hash(
            self.password_hash, password.encode('utf-8')
        )


    def __repr__(self):
        return f'<User {self.username}>'