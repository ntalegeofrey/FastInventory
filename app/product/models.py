from sqlalchemy import Column, DateTime, String, Integer
from config.database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_name = Column(String(200))
    date_created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Product %r>" % self.product_id
