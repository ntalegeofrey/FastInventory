from sqlalchemy import Column, DateTime, Integer, String
from config.database import Base
from datetime import datetime


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    location_name = Column(String(200))
    date_created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Location %r>" % self.location_id
