from sqlalchemy.orm import Session
from app.models.application import Application
from app.schemas.application_schema import ApplicationCreate

class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_application(self, app: ApplicationCreate):
        db_app = Application(**app.dict())
        self.db.add(db_app)
        self.db.commit()
        self.db.refresh(db_app)
        return db_app

    def get_application(self, app_id: int):
        return self.db.query(Application).filter(Application.id == app_id).first()

    def get_all_applications(self, skip: int = 0, limit: int = 10):
        return self.db.query(Application).offset(skip).limit(limit).all()