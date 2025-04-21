from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("DB_USERNAME", "username")
password = os.getenv("DB_PASSWORD", "password")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "3306")
database = os.getenv("DB_NAME", "database")

conn_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(conn_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()