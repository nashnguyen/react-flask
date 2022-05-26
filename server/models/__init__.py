import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv('.env')

engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
# For querying
Base.query = db_session.query_property()


class Salary(Base):
    __tablename__ = "salary"
    id = Column(Integer, unique=True, primary_key=True)
    player = Column(String(40), nullable=False)
    season = Column(String(10), nullable=False)
    salary = Column(Integer)
