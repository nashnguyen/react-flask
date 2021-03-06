import os

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from sqlalchemy_utils import create_database, database_exists

from models import db_session
from schema import schema


def create_app():
    app = Flask(__name__)

    # add CORS
    CORS(app)

    # create databases if not exists
    if not database_exists(os.environ.get('DATABASE_URL')):
        create_database(os.environ.get('DATABASE_URL'))

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql', schema=schema, graphiql=True  # for having the GraphiQL interface
        ),
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
