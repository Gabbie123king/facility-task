from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database Connection Variable
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/facility"

# Create a PostgreSQL database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
