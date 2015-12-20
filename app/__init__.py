from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo:todo@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
from app import views, models
