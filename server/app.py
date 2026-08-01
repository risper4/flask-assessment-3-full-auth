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
            return {'error' : '401 Unauthorized'}, 401



class CheckSession(Resource) :
    def check_session(self) :
        if session.get('user_id') :
            user = User.query.filter(User.id == session['user_id']).first()

            return UserSchema().dump(user), 200

        else :
            return {'error' : '401 Unauthorized'}


class Logout(Resource) :
    def post (self) :
        session['user_id'] = None
        return {}, 401


class Tasks(Resource) :
    def get (self) :
        tasks = Task.query.all()

        return TaskSchema(many=True).dump(tasks)

    def post(self) :
        task = Task(
            name = request.get_json()['name'],
            description = request.get_json()['description'],
            mark_as_compete = request.get_json()['mark_as_complete'],
            user_id = session['user_id']
        )

        try :
            db.session.add(task)
            db.session.commit()
            return TaskSchema().dump(task)

        except IntegrityError :
            return {'error' : '401 Unauthorized'}, 422



api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Tasks, '/tasks', endpoint='tasks')

if __name__ == '__main__' :
    app.run(port=5555, debug=True)