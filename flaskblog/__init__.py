from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '206c08ce6ded1fdc4b45aa6c224af8b4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # a relative path from the current file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flaskblog import routes
