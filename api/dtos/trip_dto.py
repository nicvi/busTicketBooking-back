from pydantic import BaseModel

class TripCreateDTO(BaseModel):
    bus_id: int
    route_id: int
    seats_occupied: int

class TripResponseDTO(BaseModel):
    id: int
    bus_id: int
    route_id: int
    seats_occupied: int

    class Config:
        orm_mode = True
