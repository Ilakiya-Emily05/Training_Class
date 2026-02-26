from sqlalchemy.orm import Session

from app.models.job import Job
from app.repositories.job_repository import JobRepository
from app.exceptions.custom_exceptions import JobNotFoundException


class JobService:

    @staticmethod
    def create_job(db: Session, title: str, description: str, salary: int, company_id: int) -> Job:
        job = Job(
            title=title,
            description=description,
            salary=salary,
            company_id=company_id
        )
        return JobRepository.create(db, job)

    @staticmethod
    def get_job(db: Session, job_id: int) -> Job:
        job = JobRepository.get_by_id(db, job_id)
        if not job:
            raise JobNotFoundException()
        return job

    @staticmethod
    def list_jobs(db: Session, skip: int, limit: int):
        return JobRepository.get_all(db, skip, limit)

    @staticmethod
    def update_job(db: Session, job_id: int, **kwargs) -> Job:
        job = JobRepository.get_by_id(db, job_id)
        if not job:
            raise JobNotFoundException()

        for key, value in kwargs.items():
            if value is not None:
                setattr(job, key, value)

        return JobRepository.update(db, job)

    @staticmethod
    def delete_job(db: Session, job_id: int):
        job = JobRepository.get_by_id(db, job_id)
        if not job:
            raise JobNotFoundException()
        JobRepository.delete(db, job)