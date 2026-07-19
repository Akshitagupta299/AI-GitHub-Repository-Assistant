from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

engine = create_engine(settings.DATABASE_URL) # connect fastapi to postgresql database using sqlalchemy

# create a session for every request to the database and close it after the request is completed
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base() # create a base class for all the models to inherit from