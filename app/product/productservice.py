from fastapi import Depends, HTTPException, status
from .models import Product
from sqlalchemy.orm import Session
from config.database import get_db


class ProductService:
    def get_all(db: Session = Depends(get_db)):

        return db.query(Product).order_by(Product.date_created).all()

    def createProduct(product_name: str, db: Session = Depends(get_db)):
        product_create = Product(product_name=product_name)

        try:
            db.add(product_create)
            db.commit()
            db.refresh(product_create)
        except:
            return "There Was an issue while add a new Product"

        return product_create
