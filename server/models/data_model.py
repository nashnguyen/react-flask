from models import db


class DataModel(db.Model):
    __tablename__ = "data_model"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<DataModel {self.name}>"
