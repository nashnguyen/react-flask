from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_migrate import Migrate
from api.config import Config

app = Flask(__name__)
CORS(app)


def create_app():
    app.config.from_object(Config)

    # initialize Flask SQLALchemy with this flask app
    db.init_app(app)
    Migrate(app, db)

    return app
