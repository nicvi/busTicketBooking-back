from pydantic import BaseModel


class BusCreateDTO(BaseModel):
    bus_number: str
    number_of_seats: int
    amenities: list[str]

class BusResponseDTO(BaseModel):
    id: int
    bus_number: str
    number_of_seats: int
    amenities: list[str]

    class Config:
        orm_mode = True
