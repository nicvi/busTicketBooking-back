from pydantic import BaseModel
from datetime import datetime

class RouteCreateDTO(BaseModel):
    origin_city: str
    destination_city: str
    departure_date: datetime

class RouteResponseDTO(BaseModel):
    id: int
    origin_city: str
    destination_city: str
    departure_date: datetime

    class Config:
        orm_mode = True
