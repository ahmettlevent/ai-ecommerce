import os
import secrets
from urllib.parse import quote

# SECRET_KEY = secrets.token_urlsafe(16)
SECRET_KEY = "ahmet"

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:%s@127.0.0.1:3306/prod-db' % quote(
    'UQ@sGxOBYit{WJp/c2Ju')

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False