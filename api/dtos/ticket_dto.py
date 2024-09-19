from pydantic import BaseModel


class TicketCreateDTO(BaseModel):
    booking_id: int
    seat_number: int

class TicketResponseDTO(BaseModel):
    id: int
    booking_id: int
    seat_number: int

    class Config:
        orm_mode = True
