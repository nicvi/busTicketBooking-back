from pydantic import BaseModel
from typing import Optional, List

class BusCreateDTO(BaseModel):
    bus_number: str
    number_of_seats: int
    amenities: List[str]  # List of amenities

class BusResponseDTO(BaseModel):
    id: int
    bus_number: str
    number_of_seats: int
    amenities: List[str]

    class Config:
        orm_mode = True
