from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mysql.connector import Error

# Create a SQLAlchemy engine using the MySQL connector
engine = create_engine('mysql+mysqlconnector://root:sandun123@localhost:3305/StudentManagementSystem(SMS)', echo=True)

# Create a sessionmaker bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Log success of connection or failure
def create_db_connection():
    try:
        engine.connect()
        print("Connection to MySQL DB successful")
        return engine
    except Error as e:
        print(f"The error '{e}' occurred while trying to connect to the database")
        return None
