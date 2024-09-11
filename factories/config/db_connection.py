from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5439/busTicketBooking"

# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# try:
#     with engine.connect() as connection:
#         print("Successfully connected to the database.")
# except Exception as e:
#     print(f"Failed to connect to the database. Error: {e}")

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for models to inherit from
Base = declarative_base()