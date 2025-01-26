from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL for SQLite
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for declarative models
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to initialize database (run this function in main.py to avoid circular import)
def initialize_database():
    from app.services.models import User, Transaction  # Import here to avoid circular import
    Base.metadata.create_all(bind=engine)
