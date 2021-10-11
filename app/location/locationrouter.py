from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db

# from .models import Location
from .locationservice import LocationService


router = APIRouter(prefix="/location", tags=["Locations"])


@router.get("/")
def getAllLocation(db: Session = Depends(get_db)):
    return LocationService.get_all(db=db)


@router.post("/")
def createLocation(location_name: str, db: Session = Depends(get_db)):
    return LocationService.create(location_name=location_name, db=db)
