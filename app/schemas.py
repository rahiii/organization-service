from typing import List, Union  # Import Union for Python 3.8 compatibility
from pydantic import BaseModel

class OrganizationBase(BaseModel):
    name: str
    description: Union[str, None] = None  # Changed `|` to `Union`
    contact_email: Union[str, None] = None
    website_url: Union[str, None] = None
    profile_picture: Union[str, None] = None

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(BaseModel):  # Added this class for update functionality
    name: Union[str, None] = None
    description: Union[str, None] = None
    contact_email: Union[str, None] = None
    website_url: Union[str, None] = None
    profile_picture: Union[str, None] = None

class Organization(OrganizationBase):
    id: int

    class Config:
        from_attributes = True

