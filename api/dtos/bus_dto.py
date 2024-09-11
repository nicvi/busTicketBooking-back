from pydantic import BaseModel
from typing import List

class BusCreateDTO(BaseModel):
    bus_number: str
    number_of_seats: int
    amenities: List[str]

class BusResponseDTO(BaseModel):
    id: int
    bus_number: str
    number_of_seats: int
    amenities: List[str]

    class Config:
        orm_mode = True
