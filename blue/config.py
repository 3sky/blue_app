# Postgres connection file
from blue import app
SQLALCHEMY_DATABASE_URI = 'postgresql://sky:mypassword@localhost/chart_app'
SQLALCHEMY_TRACK_MODIFICATIONS = True
