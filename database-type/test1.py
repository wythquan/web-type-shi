import sqlite3
from sqlalchemy import create_engine, Column, String, Integer, Talbe, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import string

db_url = "sqlite:///~/my_git/web-type-shi/http-type-shi/test.db"

engine = create_engine(db_url)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
    