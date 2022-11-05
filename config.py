import os

USER = os.getenv("SQL_USER")
PASSWORD = os.getenv("SQL_PASSWORD")
DB = os.getenv("SQL_DB")
HOST = os.getenv("SQL_HOST")

SQL_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB}"