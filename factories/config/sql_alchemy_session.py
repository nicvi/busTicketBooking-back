from sqlalchemy.orm import Session

from .db_connection import SessionLocal


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
