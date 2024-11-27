# app/models.py

from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    contact_email = Column(String(255), nullable=True)
    website_url = Column(String(255), nullable=True)
    profile_picture = Column(String(255), nullable=True)

