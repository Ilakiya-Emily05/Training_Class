from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.auth_controller import AuthController

router = APIRouter(prefix="/auth", tags=["Auth"])
controller = AuthController()


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return {"access_token": controller.login(db, email, password)}