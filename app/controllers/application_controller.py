from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.application_schema import LoanApplicationCreate, LoanApplicationUpdateStatus, LoanApplicationOut
from app.services.application_service import ApplicationService
from app.core.database import SessionLocal

router = APIRouter(prefix="/loan-applications", tags=["Loan Applications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LoanApplicationOut)
def apply_loan(application: LoanApplicationCreate, db: Session = Depends(get_db)):
    return ApplicationService(db).create_application(application)

@router.get("/", response_model=List[LoanApplicationOut])
def list_applications(skip: int = 0, limit: int = Query(default=10, le=100), db: Session = Depends(get_db)):
    return ApplicationService(db).list_applications(skip=skip, limit=limit)

@router.get("/{app_id}", response_model=LoanApplicationOut)
def get_application(app_id: int, db: Session = Depends(get_db)):
    app = ApplicationService(db).get_application(app_id)
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app

@router.put("/{app_id}/status", response_model=LoanApplicationOut)
def update_status(app_id: int, update: LoanApplicationUpdateStatus, db: Session = Depends(get_db)):
    updated = ApplicationService(db).update_status(app_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="Application not found")
    return updated