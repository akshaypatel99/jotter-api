from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Create a database URL for SQLAlchemy
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# Try to connect to our database
# while True:
#     try:
#         # Connect to an existing database
#         conn = psycopg2.connect(
#             database='jotter_db', user='postgres', password='bouncer99', host='localhost', cursor_factory=RealDictCursor)
#         # Open a cursor to perform database operations
#         cur = conn.cursor()
#         print("Db connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to db failed")
#         print("Error: ", error)
#         time.sleep(3)
