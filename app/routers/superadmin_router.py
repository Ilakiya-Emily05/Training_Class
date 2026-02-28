from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.superadmin_controller import SuperAdminController
from app.dependencies.rbac import require_roles

router = APIRouter(prefix="/superadmin", tags=["SuperAdmin"])
controller = SuperAdminController()


@router.post("/assets")
def create_asset(
    data: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles("SUPERADMIN"))
):
    return controller.create_asset(db, data)