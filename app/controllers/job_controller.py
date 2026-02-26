from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.job_schema import JobCreate, JobResponse
from app.services.job_service import JobService
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return JobService.create_job(db, job)

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    return JobService.get_job(db, job_id)

@router.get("/", response_model=list[JobResponse])
def list_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return JobService.list_jobs(db, skip, limit)