from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Import List for Python 3.8 compatibility
from app import models, schemas, crud
from app.database import SessionLocal, engine

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Organization Profile Service", version="1.0.0")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Organization Profile Service!"}

@app.post("/organizations/", response_model=schemas.Organization, status_code=201, tags=["Organizations"])
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    return crud.create_organization(db=db, organization=organization)

@app.get("/organizations/", response_model=List[schemas.Organization], tags=["Organizations"])  # Changed list to List
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = crud.get_organizations(db, skip=skip, limit=limit)
    return organizations

@app.get("/organizations/{organization_id}", response_model=schemas.Organization, tags=["Organizations"])
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    db_org = crud.get_organization(db=db, organization_id=organization_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org

@app.put("/organizations/{organization_id}", response_model=schemas.Organization, tags=["Organizations"])
def update_organization(organization_id: int, organization: schemas.OrganizationUpdate, db: Session = Depends(get_db)):
    updated_org = crud.update_organization(db=db, organization_id=organization_id, organization=organization)
    if updated_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return updated_org

@app.delete("/organizations/{organization_id}", response_model=schemas.Organization, tags=["Organizations"])
def delete_organization(organization_id: int, db: Session = Depends(get_db)):
    deleted_org = crud.delete_organization(db=db, organization_id=organization_id)
    if deleted_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return deleted_org

