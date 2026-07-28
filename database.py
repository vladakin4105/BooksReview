import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Incarcam variabilele de mediu din .env
load_dotenv()

# Preluam link-ul de conexiune catre Azure din .env (sau lasam SQLite ca fallback daca nu exista)
SQLALCHEMY_DATABASE_URL = os.getenv(
    "AZURE_SQL_URL", 
    "sqlite:///./book_reviews.db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()