from requests import session
from models import db


class Salary(db.Model):
    __tablename__ = "salary"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    player = db.Column(db.String(40), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f"<Id: {self.id}>"
