from datetime import datetime

from pydantic import BaseModel


class BookingCreateDTO(BaseModel):
    user_id: int
    booking_date: datetime
    status: str
    trip_id: int
    seat_numbers: list[int]

class BookingResponseDTO(BaseModel):
    id: int
    user_id: int
    booking_date: datetime
    status: str
    trip_id: int
    # seat_numbers: list[int]

    class Config:
        orm_mode = True
