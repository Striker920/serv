from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from flask_news.app1 import models, views

db.create_all()

# .env
# DATABASE_URI=sqlite:///db.sqlite3
# SECRET_KEY=YOUR_SECRET_KEY