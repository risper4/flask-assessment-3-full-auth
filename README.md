# Flask Full Authentication Backend System

### By : Risper Gichia


## Project description

* The Full Auth Backend System is a simple authentication and authorization system that involves :
    - Endpoints
    - Models
    - SQLite Database
    - Seeding examples
    - Mock client frontend interface

* The system can :
    * Authenticate users as they :
        - Signup
        - Login
        - Logout
        -Check session
    * Authorizes users to :
        - Display a user's task
        - Add a new task
        - Updates a user's post
        - Deletes a user's specific post


## Installations
    1. App
        - pipenv install
        - pipenv shell
    
    2. Database (models.py)
        - flask db init
        - flask db migrate -m 'message about your migration here'
        - flask db upgrade head

    3. Seeding (seed.py)
        - python3 seed.py

    4. Running endpoints (app.py)
        - python3 app.py


## Instructions

    - Signup : `http://127.0.0.1:5555/signup`
    - Login : `http://127.0.0.1:5555/login`
    - Check sessions : `http://127.0.0.1:5555/check_session`
    - Logout : `http://127.0.0.1:5555/logout`

    - Display all a user's post : `http://127.0.0.1:5555/tasks`
    - Add a new task to the user's account : `http://127.0.0.1:5555/tasks`
    - Updates a user's task : `http://127.0.0.1:5555/tasks/<int:id>`
    - Delete a user's task : `http://127.0.0.1:5555/tasks/<int:id>`


## Dependancies
    * flask = "2.2.2"
    * flask-sqlalchemy = "3.0.3"
    * Werkzeug = "2.2.2"
    * marshmallow = "3.20.1"
    * faker = "15.3.2"
    * flask-migrate = "4.0.0"
    * flask-restful = "0.3.9"
    * importlib-metadata = "6.0.0"
    * importlib-resources = "5.10.0"
    * pytest = "7.2.0"
    * flask-bcrypt = "1.0.1"


### Access
* Github : `https://github.com/risper4/flask_assessment_2.git`


### Contact 
    * Github : `risper4`
