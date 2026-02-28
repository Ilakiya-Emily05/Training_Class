from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.employee_controller import EmployeeController
from app.dependencies.rbac import require_roles

router = APIRouter(prefix="/employee", tags=["Employee"])
controller = EmployeeController()


@router.post("/request")
def request_asset(
    data: dict,
    db: Session = Depends(get_db),
    user=Depends(require_roles("EMPLOYEE"))
):
    return controller.request_asset(db, user.id, data)