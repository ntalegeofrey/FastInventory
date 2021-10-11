from pydantic import BaseModel


class LocationSchema(BaseModel):
    location_name: str
