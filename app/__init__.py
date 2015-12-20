from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
app = Flask(__name__, static_url_path='/static')
csrf = CsrfProtect()
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo:todo@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
csrf.init_app(app)
db = SQLAlchemy(app)
from app import views, models
