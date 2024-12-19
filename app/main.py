# app/main.py
from kafka import KafkaProducer
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List  # Import List for Python 3.8 compatibility
from app import models, schemas, crud
from app.database import SessionLocal, engine
import json

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ORGANIZATIONS", version="1.0.0")



producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event(topic, event_data):
    producer.send(topic, event_data)
    producer.flush()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Yara's Organization Profile Service!"}

@app.post("/organizations/", response_model=schemas.Organization, status_code=201, tags=["Organizations"])
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    org = crud.create_organization(db=db, organization=organization)
    publish_event("organizations_topic", {"action": "create", "organization": org})
    return org

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
    publish_event("organizations_topic", {"action": "delete", "organization_id": organization_id})
    return deleted_org

for route in app.routes:
    print(f"Path: {route.path}, Name: {route.name}, Methods: {route.methods}")
