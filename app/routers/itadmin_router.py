from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.itadmin_controller import ITAdminController
from app.dependencies.rbac import require_roles

router = APIRouter(prefix="/itadmin", tags=["IT Admin"])
controller = ITAdminController()


@router.post("/assign")
def assign_asset(
    asset_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles("SUPERADMIN", "IT_ADMIN"))
):
    return controller.assign_asset(db, asset_id, user_id)


@router.post("/approve-request")
def approve_request(
    request_id: int,
    asset_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles("SUPERADMIN", "IT_ADMIN"))
):
    return controller.approve_request(db, request_id, asset_id, user.id)