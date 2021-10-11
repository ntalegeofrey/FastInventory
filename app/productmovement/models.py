from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base
from datetime import datetime
from location.models import Location
from product.models import Product


class ProductMovement(Base):
    __tablename__ = "productmovements"

    movement_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    qty = Column(Integer)
    from_location = Column(Integer, ForeignKey("locations.id"))
    to_location = Column(Integer, ForeignKey("locations.id"))
    movement_time = Column(DateTime, default=datetime.utcnow)

    product = relationship(Product, foreign_keys=product_id)
    fromLoc = relationship(Location, foreign_keys=from_location)
    toLoc = relationship(Location, foreign_keys=to_location)

    def __repr__(self):
        return "<ProductMovement %r>" % self.movement_id
