from random import choice as rc

from faker import Faker

from app import app
from models import User, Task
from config import db

faker = Faker()


with app.app_context() : 

    print('Delete all records...')
    User.query.delete()
    Task.query.delete()

    fake = Faker()

    print('Create users...')

    users = []
    usernames = []
    passwords = ['password', 'pass123', 'mom101', 'sonder27', 'random5']

    for i in range(10) :
        username = fake.first_name()
        while username in usernames :
            username = fake.first_name()

        usernames.append(username)

        user = User(username=username)
        user.password_hash = rc(passwords)

        users.append(user)

    db.session.add_all(users)


    print('Print passwords...')
    tasks = []

    tasks.append(Task(name='Cook supper', description='Go to bed early', mark_as_complete=True, user_id=3))
    tasks.append(Task(name='Wash the dishes', description='Fix the dishwasher', mark_as_complete=False, user_id=1))
    tasks.append(Task(name='Buy groceries', description='Go to carefour', mark_as_complete=True, user_id=2))
    tasks.append(Task(name='Walk Simba to the park', description='Go to the park', mark_as_complete=False, user_id=2))
    tasks.append(Task(name='Meet up with Ryan', description='Be at Parkinton hotel', mark_as_complete=False, user_id=4))

    db.session.add_all(tasks)

    print('Commiting users and tasks to the database')
    db.session.commit()
    print('Complete')