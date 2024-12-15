from sqlalchemy.orm import Session
from app import models, schemas


def get_organization(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()

#function to add HATEOAS and support for links
def add_hateoas_to_organization(org: dict):
    return {
        **org,
        "_links": {
            "self": f"/organizations/{org['id']}",
            "update": f"/organizations/{org['id']}",
            "delete": f"/organizations/{org['id']}",
            "events": f"/organization/event/{org['id']}"
        }
    }

#GET calls the function to show HATEOAS links
def get_organizations_with_links(db: Session, skip: int = 0, limit: int = 100):
    organizations = db.query(models.Organization).offset(skip).limit(limit).all()
    return [
        add_hateoas_to_organization({
            "id": org.id,
            "name": org.name,
            "description": org.description,
            "contact_email": org.contact_email,
            "website_url": org.website_url,
            "profile_picture": org.profile_picture
        }) 
        for org in organizations
    ]



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
