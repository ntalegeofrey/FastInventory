from pydantic import BaseModel


class Product(BaseModel):
    product_name: str
