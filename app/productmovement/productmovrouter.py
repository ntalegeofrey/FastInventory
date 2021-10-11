from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from .productmovservice import ProductMovService
from .schema import ProductMovList

from config.database import get_db


router = APIRouter(prefix="/productmov", tags=["ProductsMove"])


@router.get("/")
def getallMove(db: Session = Depends(get_db)):
    return ProductMovService.get_all(db)


@router.post("/")
def createMove(
    productId: int,
    qty: int,
    fromLocation: int,
    toLocation: int,
    db: Session = Depends(get_db),
):

    return ProductMovService.create(
        productId=productId,
        qty=qty,
        fromLocation=fromLocation,
        toLocation=toLocation,
        db=db,
    )


@router.put("/{id}")
def updateMove(
    id: int,
    productId: int,
    qty: int,
    fromLocation: int,
    toLocation: int,
    db: Session = Depends(get_db),
):
    return ProductMovService.update(
        id=id,
        productId=productId,
        qty=qty,
        fromLocation=fromLocation,
        toLocation=toLocation,
        db=db,
    )


@router.delete("/{id}")
def deleteMove(id: int, db: Session = Depends(get_db)):
    return ProductMovService.delete(id=id, db=db)
