from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from .productservice import ProductService

from config.database import get_db


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def getAll(db: Session = Depends(get_db)):
    return ProductService.get_all(db=db)


@router.post("/")
def createProduct(product_name: str, db: Session = Depends(get_db)):
    return ProductService.createProduct(product_name=product_name, db=db)
