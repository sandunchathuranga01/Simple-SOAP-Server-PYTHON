from sqlalchemy import Column, Integer, String
from Component.DB_config import Base

# Define the Item table structure
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)
