from sqlalchemy.orm import Session
from app.models.loan_product import LoanProduct
from app.schemas.product_schema import LoanProductCreate, LoanProductUpdate
from typing import List, Optional

class LoanProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: LoanProductCreate) -> LoanProduct:
        db_product = LoanProduct(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_by_id(self, product_id: int) -> Optional[LoanProduct]:
        return self.db.query(LoanProduct).filter(LoanProduct.id == product_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[LoanProduct]:
        return self.db.query(LoanProduct).offset(skip).limit(limit).all()

    def update(self, product_id: int, update_data: LoanProductUpdate) -> Optional[LoanProduct]:
        db_product = self.get_by_id(product_id)
        if not db_product:
            return None
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(db_product, field, value)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete(self, product_id: int) -> bool:
        db_product = self.get_by_id(product_id)
        if not db_product:
            return False
        self.db.delete(db_product)
        self.db.commit()
        return True