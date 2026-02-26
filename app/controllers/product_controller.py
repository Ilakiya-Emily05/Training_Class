from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.product_schema import LoanProductCreate, LoanProductUpdate, LoanProductOut
from app.services.product_service import ProductService
from app.core.database import SessionLocal

router = APIRouter(prefix="/loan-products", tags=["Loan Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LoanProductOut)
def create_product(product: LoanProductCreate, db: Session = Depends(get_db)):
    return ProductService(db).create_product(product)

@router.get("/", response_model=List[LoanProductOut])
def list_products(skip: int = 0, limit: int = Query(default=10, le=100), db: Session = Depends(get_db)):
    return ProductService(db).list_products(skip=skip, limit=limit)

@router.get("/{product_id}", response_model=LoanProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductService(db).get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=LoanProductOut)
def update_product(product_id: int, update: LoanProductUpdate, db: Session = Depends(get_db)):
    updated = ProductService(db).update_product(product_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ProductService(db).delete_product(product_id)
    return None