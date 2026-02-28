from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so SQLAlchemy registers them
from app.models.user import User
from app.models.department import Department
from app.models.asset import Asset
from app.models.asset_assignment import AssetAssignment
from app.models.asset_request import AssetRequest