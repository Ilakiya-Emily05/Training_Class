from sqlalchemy.orm import Session

from app.models.application import Application
from app.repositories.application_repository import ApplicationRepository
from app.repositories.user_repository import UserRepository
from app.repositories.job_repository import JobRepository
from app.exceptions.custom_exceptions import NotFoundException, ConflictException


class ApplicationService:

    @staticmethod
    def apply_for_job(db: Session, user_id: int, job_id: int) -> Application:
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise NotFoundException("User not found")

        job = JobRepository.get_by_id(db, job_id)
        if not job:
            raise NotFoundException("Job not found")

        application = Application(
            user_id=user_id,
            job_id=job_id,
            status="applied"
        )
        return ApplicationRepository.create(db, application)

    @staticmethod
    def get_application(db: Session, application_id: int) -> Application:
        application = ApplicationRepository.get_by_id(db, application_id)
        if not application:
            raise NotFoundException("Application not found")
        return application

    @staticmethod
    def list_user_applications(db: Session, user_id: int):
        return ApplicationRepository.get_by_user(db, user_id)

    @staticmethod
    def update_status(db: Session, application_id: int, status: str) -> Application:
        application = ApplicationRepository.get_by_id(db, application_id)
        if not application:
            raise NotFoundException("Application not found")

        allowed = {"applied", "shortlisted", "rejected"}
        if status not in allowed:
            raise ConflictException("Invalid application status")

        application.status = status
        return ApplicationRepository.update(db, application)