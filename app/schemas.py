# app/schemas.py

from pydantic import BaseModel
from typing import Optional

class OrganizationBase(BaseModel):
    name: str
    description: Optional[str] = None
    contact_email: Optional[str] = None
    website_url: Optional[str] = None
    profile_picture: Optional[str] = None  # Could be a URL or a file path

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(OrganizationBase):
    pass

class OrganizationInDBBase(OrganizationBase):
    id: int

    class Config:
        orm_mode = True

class Organization(OrganizationInDBBase):
    pass

