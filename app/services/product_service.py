from app.models.loan_product import LoanProduct
from app.core.database import SessionLocal

class ProductService:
    def __init__(self):
        self.db = SessionLocal()

    def get_product(self, product_id: int):
        return self.db.query(LoanProduct).filter(LoanProduct.id == product_id).first()

    def create_product(self, product: LoanProduct):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product