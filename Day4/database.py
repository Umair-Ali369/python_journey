
from sqlalchemy.orm.session import Session


from sqlalchemy.orm.session import Session


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "postgresql://postgres:khan@localhost:5432/global_system_db"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker[Session](autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
       db.close()

def create_tables():

    import Models
    
    print("Creating tables in PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
    