from config import SQL_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session


engine = create_engine(SQL_URL)
# engine = create_engine(SQL_URL, echo=True, future=True)
session = Session(engine)

Base = declarative_base()

