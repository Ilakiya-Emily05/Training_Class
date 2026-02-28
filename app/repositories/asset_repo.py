from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.asset import Asset
from app.core.pagination import PaginationParams


class AssetRepository:
    def create(self, db: Session, asset: Asset) -> Asset:
        db.add(asset)
        db.commit()
        db.refresh(asset)
        return asset

    def get_by_id(self, db: Session, asset_id: int) -> Asset | None:
        return db.query(Asset).filter(Asset.id == asset_id).first()

    def get_by_tag(self, db: Session, asset_tag: str) -> Asset | None:
        return db.query(Asset).filter(Asset.asset_tag == asset_tag).first()

    def list(
        self,
        db: Session,
        pagination: PaginationParams,
        status: str | None = None,
        department_id: int | None = None
    ):
        query = db.query(Asset)

        if status:
            query = query.filter(Asset.status == status)

        if department_id:
            query = query.filter(Asset.department_id == department_id)

        if pagination.sort_by:
            column = getattr(Asset, pagination.sort_by, None)
            if column is not None:
                query = query.order_by(
                    asc(column) if pagination.order == "asc" else desc(column)
                )

        return query.offset(pagination.offset).limit(pagination.size).all()