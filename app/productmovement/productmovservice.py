from fastapi import Depends, HTTPException
from .models import ProductMovement
from product.models import Product
from sqlalchemy.orm import Session
from config.database import get_db


class ProductMovService:
    def get_all(db: Session = Depends(get_db)):

        return db.query(ProductMovement).order_by(ProductMovement.movement_time).all()

    def create(
        productId: int,
        qty: int,
        fromLocation: int,
        toLocation: int,
        db: Session = Depends(get_db),
    ):
        new_movement = ProductMovement(
            product_id=productId,
            qty=qty,
            from_location=fromLocation,
            to_location=toLocation,
        )

        try:
            db.add(new_movement)
            db.commit()
            db.refresh(new_movement)
        except:
            return "There Was an issue while add a new Movement"

        return new_movement

    def update(
        id: int,
        productId: int,
        qty: int,
        fromLocation: int,
        toLocation: int,
        db: Session = Depends(get_db),
    ):
        movement_update = (
            db.query(ProductMovement).filter(ProductMovement.id == id).first()
        )

        try:
            movement_update.product_id = productId
            movement_update.qty = qty
            movement_update.from_location = fromLocation
            movement_update.to_location = toLocation

            db.commit()
        except:
            return "There was an issue while updating the Product Movement"

        return movement_update

    def delete(id: int, db: Session = Depends(get_db)):
        movement_delete = (
            db.query(ProductMovement).filter(ProductMovement.id == id).first()
        )

        try:
            db.delete(movement_delete)
            db.commit()
        except:
            return "There was an issue while deleteing the Prodcut Movement"
