from typing import Optional
from pydantic import BaseModel
from product.schema import Product
from location.schema import LocationSchema


class ProductMov(BaseModel):
    movement_id: int
    product_id: int
    qty: int
    from_location: int
    to_location: int


class ProductMovList(ProductMov):
    product: Product
    fromLoc: ProductMov

    class Config:
        orm_mode = True
