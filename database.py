import os
import time
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

# 1. Grab the URL injected by Docker Compose
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Add connection timeout arguments to the driver
engine = create_engine(
    DATABASE_URL,
    connect_args={"connect_timeout": 5}
)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

# 3. Robust table creation loop to handle Docker initialization lag
from models import Post, User

def initialize_database():
    retries = 5
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("Successfully connected to the database and initialized schemas!")
            break
        except OperationalError:
            retries -= 1
            print(f"Database is still booting up... Retrying in 2 seconds ({retries} retries left)")
            time.sleep(2)
            
    if retries == 0:
        raise Exception("Could not connect to the database container.")

# Run the initialization loop safely
initialize_database()
