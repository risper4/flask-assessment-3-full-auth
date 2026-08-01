from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, api, db
from models import User, Task
from schema import UserSchema, TaskSchema


class Signup(Resource) :
    def post(self) :

        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User(
            username=username
        )
        user.password_hash = password

        try :
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return UserSchema().dump(user), 200
        except IntegrityError :
            return {'error' : '422 Unprocessed Entity'}, 422



class Login(Resource) :
    def post(self) :
        username = request.get_json()['username']

        user = User.query.filter(User.username == username).first()

        password = request.get_json()['password']

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return UserSchema().dump(user)

        else :
            return {'error' : 'Unauthorized access'}, 401



api.add_resource(Signup, '/signup', endpoint='signup')

if __name__ == '__main__' :
    app.run(port=5555, debug=True)