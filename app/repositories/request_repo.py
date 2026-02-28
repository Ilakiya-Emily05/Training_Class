from sqlalchemy.orm import Session
from app.models.asset_request import AssetRequest


class RequestRepository:
    def create(self, db: Session, request: AssetRequest) -> AssetRequest:
        db.add(request)
        db.commit()
        db.refresh(request)
        return request

    def get_by_id(self, db: Session, request_id: int) -> AssetRequest | None:
        return db.query(AssetRequest).filter(AssetRequest.id == request_id).first()

    def list(self, db: Session, status: str | None = None):
        query = db.query(AssetRequest)
        if status:
            query = query.filter(AssetRequest.status == status)
        return query.all()

    def update(self, db: Session, request: AssetRequest) -> AssetRequest:
        db.commit()
        db.refresh(request)
        return request