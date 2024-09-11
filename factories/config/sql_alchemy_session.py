from sqlalchemy.orm import Session
from .db_connection import SessionLocal

def get_db():
    db: Session = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session for use in the dependency
    finally:
        db.close()  # Ensure the session is closed after the request