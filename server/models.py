from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import bcrypt, db


class User(db.Model) :
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    tasks = db.relationship('Task', back_populates='user')

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




class Task(db.Model) :
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String)
    marked_as_complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='tasks')

    __table_args__ = (
        db.CheckConstraint('length(description) <= 500'),
    )

    
    def __repr__(self):
        return f'<Post {self.id} : {self.name}>'