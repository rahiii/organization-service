# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas

def get_organization(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()

def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Organization).offset(skip).limit(limit).all()

def create_organization(db: Session, organization: schemas.OrganizationCreate):
    db_org = models.Organization(**organization.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

def update_organization(db: Session, organization_id: int, organization: schemas.OrganizationUpdate):
    db_org = get_organization(db, organization_id)
    if db_org:
        for key, value in organization.dict(exclude_unset=True).items():
            setattr(db_org, key, value)
        db.commit()
        db.refresh(db_org)
    return db_org

def delete_organization(db: Session, organization_id: int):
    db_org = get_organization(db, organization_id)
    if db_org:
        db.delete(db_org)
        db.commit()
    return db_org

