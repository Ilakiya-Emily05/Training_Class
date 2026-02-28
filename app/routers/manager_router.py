from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.manager_controller import ManagerController
from app.core.pagination import PaginationParams
from app.dependencies.rbac import require_roles

router = APIRouter(prefix="/manager", tags=["Manager"])
controller = ManagerController()


@router.get("/assets")
def view_department_assets(
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
    user=Depends(require_roles("MANAGER"))
):
    return controller.list_department_assets(db, pagination, user.department_id)