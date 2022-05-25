from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
from sqlalchemy_utils import create_database, database_exists

from api.config import Config

app = Flask(__name__)
CORS(app)


def create_app():
    # load config
    app.config.from_object(Config)

    # create databases if not exists
    db_url = app.config["SQLALCHEMY_DATABASE_URI"]
    if not database_exists(db_url):
        create_database(db_url)

    # initialize Flask SQLALchemy with this flask app
    db.init_app(app)
    Migrate(app, db)

    return app
