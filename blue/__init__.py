from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from jinja2 import TemplateNotFound


app = Flask(__name__)
Bootstrap(app)

from blue.guest.routes import guest_mod
from blue.user.routes import user_mod

app.register_blueprint(guest_mod, url_prefix='/')
app.register_blueprint(user_mod, url_prefix='/account/')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from blue.models import *

db.create_all()

