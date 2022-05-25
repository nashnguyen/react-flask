from flask_migrate import Migrate

from api import create_app
from models import db

app = create_app()
migrate = Migrate(app, db)


@app.cli.command("recreate_db")
def recreate_db():
    # Recreates a database when there's a new database instance
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    app.run()
