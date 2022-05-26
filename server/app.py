from api import create_app
from models import engine, Base, Salary

app = create_app()


@app.cli.command("create_db")
def create_db():
    # Creates a database when there's a new database instance
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    app.run()
