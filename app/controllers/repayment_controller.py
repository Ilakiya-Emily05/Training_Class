from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.repayment_schema import RepaymentCreate, RepaymentOut
from app.services.repayment_service import RepaymentService
from app.core.database import SessionLocal

router = APIRouter(prefix="/repayments", tags=["Repayments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RepaymentOut)
def add_repayment(repayment: RepaymentCreate, db: Session = Depends(get_db)):
    return RepaymentService(db).add_repayment(repayment)

@router.get("/loan/{loan_id}", response_model=List[RepaymentOut])
def get_repayments(loan_id: int, db: Session = Depends(get_db)):
    repayments = RepaymentService(db).get_repayments_by_loan(loan_id)
    if not repayments:
        raise HTTPException(status_code=404, detail="No repayments found")
    return repayments