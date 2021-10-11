from fastapi import Depends
from sqlalchemy.orm.session import Session
from config.database import get_db
from .models import Location
from sqlalchemy.orm import Session


class LocationService:
    def get_all(db: Session = Depends(get_db)):
        return db.query(Location).order_by(Location.date_created).all()

    def create(location_name: str, db: Session = Depends(get_db)):
        new_location = Location(location_name=location_name)
        try:
            db.add(new_location)
            db.commit()
            db.refresh()
        except:
            return "There Was an issue while add a new Location"
        return new_location

    def update(id: int, location_name: str, db: Session = Depends(get_db)):
        location_update = db.query(Location).filter(Location.id == id).first()
        try:

            location_update.location_id = location_name

            db.commit()
        except:
            return "There Was an issue while a update Location"

        return location_update

    def delete(id: int, db: Session = Depends(get_db)):
        location_delete = db.query(Location).filter(Location.id == id).first()
        try:

            db.delete(location_delete)

            db.commit()
        except:
            return "There Was an issue while a delete Location"

        return location_delete
