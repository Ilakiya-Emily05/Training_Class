from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.application_schema import ApplicationCreate, ApplicationResponse
from app.services.application_service import ApplicationService
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=ApplicationResponse)
def apply(application: ApplicationCreate, db: Session = Depends(get_db)):
    return ApplicationService.apply(db, application)

@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    return ApplicationService.get_application(db, application_id)