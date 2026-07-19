from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base # Every model must inherit from Base.


class User(Base): # This tells SQLAlchemy: This Python class should become a database table.
    __tablename__ = "users" # This is the name of the table in the database.

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    github_id = Column(String, unique=True)

    created_at = Column(DateTime, default=datetime.utcnow)