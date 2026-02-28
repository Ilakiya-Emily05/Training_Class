from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.auth_controller import AuthController
from app.schemas.user_schema import UserCreate

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    return AuthController.register(db, data)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    return AuthController.login(db, email, password)