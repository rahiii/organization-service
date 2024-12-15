from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List  # For Python 3.8 compatibility
from app import models, schemas, crud
from app.database import SessionLocal, engine
import asyncio
import uuid


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Organization Profile Service", version="1.0.0")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Organization Profile Service!"}

# Create a new organization w/ HATEOAS links
@app.post("/organizations/", response_model=dict, status_code=201, tags=["Organizations"])
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    db_org = crud.create_organization(db=db, organization=organization)
    return crud.add_hateoas_to_organization({
        "id": db_org.id,
        "name": db_org.name,
        "description": db_org.description,
        "contact_email": db_org.contact_email,
        "website_url": db_org.website_url,
        "profile_picture": db_org.profile_picture
    })

# Read all organizations (calls the fn to add links)
@app.get("/organizations/", response_model=List[dict], tags=["Organizations"])
def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_organizations_with_links(db, skip, limit)

# Read a single organization w/ HATEOAS
@app.get("/organizations/{organization_id}", response_model=dict, tags=["Organizations"])
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    db_org = crud.get_organization(db=db, organization_id=organization_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    return crud.add_hateoas_to_organization({
        "id": db_org.id,
        "name": db_org.name,
        "description": db_org.description,
        "contact_email": db_org.contact_email,
        "website_url": db_org.website_url,
        "profile_picture": db_org.profile_picture
    })

# Update organization w/ HATEOAS
@app.put("/organizations/{organization_id}", response_model=dict, tags=["Organizations"])
def update_organization(organization_id: int, organization: schemas.OrganizationUpdate, db: Session = Depends(get_db)):
    updated_org = crud.update_organization(db=db, organization_id=organization_id, organization=organization)
    if updated_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    return crud.add_hateoas_to_organization({
        "id": updated_org.id,
        "name": updated_org.name,
        "description": updated_org.description,
        "contact_email": updated_org.contact_email,
        "website_url": updated_org.website_url,
        "profile_picture": updated_org.profile_picture
    })

#Delete organization w/ HATEOAS 
@app.delete("/organizations/{organization_id}", response_model=dict, tags=["Organizations"])
def delete_organization(organization_id: int, db: Session = Depends(get_db)):
    deleted_org = crud.delete_organization(db=db, organization_id=organization_id)
    if deleted_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    return {
        "message": "Organization deleted successfully",
        "_links": {
            "create": "/organizations/", #create new org
            "all": "/organizations/" #read all orgs
        }
    }


tasks = {}

@app.post("/organizations/{organization_id}/start-background-task", status_code=202, tags=["Tasks"])
async def start_background_task(organization_id: int, db: Session = Depends(get_db)):
    """
    Accepts a task to process an organization asynchronously.
    Returns a task ID with status URL.
    """
  
    db_org = crud.get_organization(db=db, organization_id=organization_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")


    task_id = str(uuid.uuid4())
    tasks[task_id] = "IN_PROGRESS"

  
    asyncio.create_task(mock_background_task(organization_id, task_id))

    return JSONResponse(
        content={"task_id": task_id, "status_url": f"/tasks/{task_id}"},
        status_code=202
    )

#Asynchronous execution patterns: 

async def mock_background_task(organization_id: int, task_id: str):
    await asyncio.sleep(5)
    tasks[task_id] = f"Task completed for organization {organization_id}"

@app.get("/tasks/{task_id}", tags=["Tasks"])
async def get_task_status(task_id: str):
    status = tasks.get(task_id, "NOT_FOUND")
    if status == "NOT_FOUND":
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task_id": task_id, "status": status}
