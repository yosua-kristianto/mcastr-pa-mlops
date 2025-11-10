import os

from sqlalchemy import (
    create_engine
)

from sqlalchemy.orm import sessionmaker

def databaseConnection():
    # Build DB connection string from .env
    host = os.getenv("DATABASE_HOST")
    port = os.getenv("DATABASE_PORT")
    user = os.getenv("DATABASE_USER")
    password = os.getenv("DATABASE_PASSWORD")
    dbname = os.getenv("DATABASE_NAME")


    db_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}"

    # Create session
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("[INFO] Database Connection established")

    return session