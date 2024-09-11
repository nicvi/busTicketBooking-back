from pydantic import BaseModel
from typing import Optional

class TicketCreateDTO(BaseModel):
    booking_id: int
    seat_number: int

class TicketResponseDTO(BaseModel):
    id: int
    booking_id: int
    seat_number: int

    class Config:
        orm_mode = True