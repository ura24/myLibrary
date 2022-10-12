from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config.from_object('flask_app.config')

db = SQLAlchemy(app)
from .models import book

import flask_app.views