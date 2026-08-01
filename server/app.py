from flask import request, session
from flask_restful import Resource
from sqlalchemy import IntegrityError

from config import app, api, db





if __name__ == '__main__' :
    app.run(port=5555, debug=True)