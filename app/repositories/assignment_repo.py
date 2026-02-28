from sqlalchemy.orm import Session
from app.models.asset_assignment import AssetAssignment


class AssignmentRepository:
    def create(self, db: Session, assignment: AssetAssignment) -> AssetAssignment:
        db.add(assignment)
        db.commit()
        db.refresh(assignment)
        return assignment

    def get_active_by_asset(self, db: Session, asset_id: int) -> AssetAssignment | None:
        return (
            db.query(AssetAssignment)
            .filter(
                AssetAssignment.asset_id == asset_id,
                AssetAssignment.returned_date.is_(None)
            )
            .first()
        )

    def return_asset(
        self,
        db: Session,
        assignment: AssetAssignment,
        condition_on_return: str | None = None
    ):
        assignment.returned_date = assignment.returned_date or __import__("datetime").datetime.utcnow()
        assignment.condition_on_return = condition_on_return
        db.commit()
        db.refresh(assignment)
        return assignment